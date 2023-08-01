/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",],
    
    theme: { 
      fontFamily: {
        sans: ['Poppins', 'system-ui', 'sans-serif'],
      },
  
      extend: {
        colors: {
          primary: '#3E78B2', 
          'primary-focus':'#2A5279'
        },
        textColor:{
          'primary-focus':'#2A5279'
        }
      },
    },
  plugins: [require("daisyui")],
}

