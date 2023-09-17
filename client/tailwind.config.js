/** @type {import('tailwindcss').Config} */
export default{
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
    colors: {
      'layout-border': '#CCCCCC',
      'button': '#CCCCCC',
      'button-hover': '#AAAAAA',
      'danger': '#D23434',
      'danger-hover': '#AA0000',
      'danger-text': '#F0F0F0',
      'nav-item': '#CCCCCC',
      'nav-item-hover': '#AAAAAA',
      'nav-mobile-border': '#FFFFFF',
      'dashboard-bg': '#CCCCCC',
      'checklist-item': '#FFFFFF',
      'white': '#FFFFFF',
      'black': '#000000',
    }
  },
  plugins: [],
}
