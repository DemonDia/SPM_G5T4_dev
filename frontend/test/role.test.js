// @ts-check
const { test, expect } = require("@playwright/test");
const { faker } = require("@faker-js/faker");
const { default: login } = require("../scripts/loginScript");
const { default: delay } = require("../scripts/delay");

test("CRUD Role", async ({ page }) => {
  const url = "http://localhost:8080";
  await page.goto(url);

  const roleTitle = `${Date.now()/3}`;
  const roleDescription = "Product Manager needs to collaborate effectively with various stakeholder";

  const changedRoleTitle = `${Date.now()/2}`;
  const changedRoleDescription = "Product Manager needs to collaborate effectively with various stakeholder UPDATES!!";

  const skillSearch = "Skill_Name #1";

  // create a locator
  await login(page);
  await page.goto(`${url}/roles`);
  await page.locator('a[href="/create-role"]').waitFor();
  await page.locator('a[href="/create-role"]').click();
  const createRoleHeader = await page.textContent('text="Create a Role"');
  await expect(createRoleHeader).toBeTruthy();
  await page.locator('input[placeholder="Role Name"]').fill(roleTitle);
  await page
    .locator('textarea[placeholder="Role Description"]')
    .fill(roleDescription);
  await page.locator('button:has-text("Next: Assign Skills")').click();

  // Input Skill
  // await page.locator('input[name="pillSearch"]').waitFor();
  // await page.locator('input[name="pillSearch"]').click();
  // await page.locator('input[name="pillSearch"]').fill(skillSearch);
  // await page.keyboard.press("Enter");

  // await page.locator(`li:has-text("${skillSearch}")`).click();
  // expect(await page.isVisible(`span:has-text("${skillSearch})`)).toBeTruthy();
  await page.locator('button:has-text("Next: Confirm choices")').click();

  // Submit Roles
  await page.locator('button:has-text("Submit")').click();
  await page.locator('h1[id="submitModalLabel"]').waitFor();
  await page.goto(`${url}/roles`);
  await page.locator('a[href="/create-role"]').waitFor();
  expect(await page.isVisible(`h5:has-text("${roleTitle}")`)).toBeTruthy();
  expect(await page.isVisible(`p:has-text("${roleDescription}")`)).toBeTruthy();

  // Update Role
  await page.locator(`//h5[text()='${roleTitle}']/../..//button`).click();
  await page.locator('a:has-text("Update"):visible').click();
  await page.locator('h3:has-text("Update a Role")').waitFor();
  await page.locator('input[placeholder="Role Name"]').fill(changedRoleTitle);
  await page
    .locator('textarea[placeholder="Role Description"]')
    .fill(changedRoleDescription);
  await page.locator('button:has-text("Update Role")').click();
  // await delay(15000);
  await page.locator('h1[id="submitModalLabel"]').waitFor();
  await page.goto(`${url}/roles`);
  await page.locator('a[href="/create-role"]').waitFor();
  expect(
    await page.isVisible(`h5:has-text("${changedRoleTitle}")`)
  ).toBeTruthy();
  expect(
    await page.isVisible(`p:has-text("${changedRoleDescription}")`)
  ).toBeTruthy();

  // Delete Update
  await page
    .locator(`//h5[text()='${changedRoleTitle}']/../..//button`)
    .click();
  await page.locator('a:has-text("Delete"):visible').click();
  await page.locator(".mosha__toast").waitFor();
  await delay(7000);
  expect(
    await page.isVisible(`h5:has-text("${changedRoleTitle}")`)
  ).toBeFalsy();
  expect(
    await page.isVisible(`p:has-text("${changedRoleDescription}")`)
  ).toBeFalsy();
});
