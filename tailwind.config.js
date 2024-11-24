/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
	'./app/templates/app/**/*.html',
    './static/src/**/*.css',
	'./node_modules/daisyui/**/*.js',
      ],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui"),require('@tailwindcss/forms')],
  daisyui: {
    themes: [
      {
        mytheme: {
			"primary": "#ccdfff",
			"secondary": "#ff89ff",
			"accent": "#00ffff",
			"neutral": "#f4ffff",
		},
	  },
	],
  },
}

