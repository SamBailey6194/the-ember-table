/** @type {import('jest').Config} */
module.exports = {
  testEnvironment: "jsdom",
  testMatch: ["**/__tests__/**/*.test.js?(x)", "**/?(*.)+(spec|test).[jt]s?(x)"],
  transform: {},
};