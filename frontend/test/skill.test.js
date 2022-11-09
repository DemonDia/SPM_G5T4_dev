// @ts-check
const { test, expect } = require("@playwright/test");
const { faker } = require("@faker-js/faker");
const { default: login } = require("../scripts/loginScript");
const { default: delay } = require("../scripts/delay");

test("CRUD Skill", async ({ page }) => {
  const url = "http://localhost:8080";
  await page.goto(url);

  const skillTitle = `${Date.now()/3}`;
  const skillDescription = "Strengths and abilities individuals demonstrate that help to oversee processes, guide initiatives and steer their employees toward the achievement of goals";

  const changedSkillTitle = `${Date.now()/2}`;
  const changedSkillDescription = "Working with people from different places";

  const roleSearch = "Role_Name #1";

  // create a locator
  await login(page);
  await page.goto(`${url}/skills`);
  await page.locator('a[href="/create-skill"]').waitFor();
  await page.locator('a[href="/create-skill"]').click();
  const createSkillHeader = await page.textContent('text="Create a Skill"');
  await expect(createSkillHeader).toBeTruthy();
  await page.locator('input[placeholder="Skill Name"]').fill(skillTitle);
  await page
    .locator('textarea[placeholder="Skill Description"]')
    .fill(skillDescription);
  await page.locator('button:has-text("Next: Assign Roles")').click();

  await page.locator('button:has-text("Next: Confirm choices")').click();

  // Submit Skills
  await page.locator('button:has-text("Submit")').click();
  await page.locator('h1[id="submitModalLabel"]').waitFor();
  await page.goto(`${url}/skills`);
  await page.locator('a[href="/create-skill"]').waitFor();
  expect(await page.isVisible(`h5:has-text("${skillTitle}")`)).toBeTruthy();
  expect(await page.isVisible(`p:has-text("${skillDescription}")`)).toBeTruthy();

  // Update Skill
  await page.locator(`//h5[text()='${skillTitle}']/../..//button`).click();
  await page.locator('a:has-text("Update"):visible').click();
  await page.locator('h3:has-text("Update a Skill")').waitFor();
  await page.locator('input[placeholder="Skill Name"]').fill(changedSkillTitle);
  await page
    .locator('textarea[placeholder="Skill Description"]')
    .fill(changedSkillDescription);
  await page.locator('button:has-text("Update Skill")').click();
  // await delay(15000);
  await page.locator('h1[id="submitModalLabel"]').waitFor();
  await page.goto(`${url}/skills`);
  await page.locator('a[href="/create-skill"]').waitFor();
  expect(
    await page.isVisible(`h5:has-text("${changedSkillTitle}")`)
  ).toBeTruthy();
  expect(
    await page.isVisible(`p:has-text("${changedSkillDescription}")`)
  ).toBeTruthy();

  // Delete Update
  await page
    .locator(`//h5[text()='${changedSkillTitle}']/../..//button`)
    .click();
  await page.locator('a:has-text("Delete"):visible').click();
  await page.locator(".mosha__toast").waitFor();
  await delay(7000);
  expect(
    await page.isVisible(`h5:has-text("${changedSkillTitle}")`)
  ).toBeFalsy();
  expect(
    await page.isVisible(`p:has-text("${changedSkillDescription}")`)
  ).toBeFalsy();
});
