export default async function login(page) {
  const staffId = await page.locator('input[name="staffID"]');
  await staffId.fill("130001");

  const password = await page.locator('input[name="password"]');
  await password.fill("123456");

  await page.locator('button[type="submit"]').click();
}
