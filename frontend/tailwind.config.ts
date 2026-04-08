import type { Config } from "tailwindcss";

const config: Config = {
  content: ["./src/**/*.{js,ts,jsx,tsx,mdx}"],
  theme: {
    extend: {
      colors: {
        sand: "#F6F1E8",
        ink: "#172033",
        ember: "#B24C2D",
        moss: "#415C49",
        cloud: "#FCFBF8",
      },
      fontFamily: {
        sans: ["var(--font-sans)"],
        display: ["var(--font-display)"],
      },
      boxShadow: {
        glow: "0 30px 80px -40px rgba(23, 32, 51, 0.45)",
      },
    },
  },
  plugins: [],
};

export default config;

