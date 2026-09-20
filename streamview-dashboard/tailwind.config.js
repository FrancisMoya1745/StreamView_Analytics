/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        brand: {
          red: '#E50914',
          dark: '#121212',
          panel: '#1E1E1E',
          text: '#E5E5E5',
          muted: '#808080',
          blue: '#3b82f6',
        }
      }
    },
  },
  plugins: [],
}