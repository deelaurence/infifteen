// tailwind.config.js
module.exports = {
  mode: 'jit',
  purge: [
    // Specify paths to your Django templates to purge unused styles
    './_templates/**/*.html',
    './_templates/base.html'
    // Add more paths as needed
  ],
  theme: {
    screen: {
      sm: "480px",
      bmd: "600px",
      md: "768px",
      lg: "900px",
      xl: "1440px",
    },
    extend: {
      fontFamily: {
        sharpGrotesk: ['"Sharp Grotesk"', 'sans-serif'],
      },
      colors: {
        shade1: "#212A31",
        shade2: "#2E3944",
        shade3: "#12E466",
        shade4: "#748D92",
        shade5: "#D3D9D4",
        shade6: "#B6A39F"
      },
    },
  },
  plugins: [],
}
