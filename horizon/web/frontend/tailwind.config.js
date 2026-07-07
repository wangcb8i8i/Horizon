/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: "class",
  theme: {
    extend: {
      fontFamily: {
        display: ["Sora", "ui-sans-serif", "system-ui", "sans-serif"],
        body: ["Geist", "ui-sans-serif", "system-ui", "sans-serif"],
        mono: ['"JetBrains Mono"', "ui-monospace", "SF Mono", "Menlo", "monospace"],
      },
      colors: {
        horizon: {
          bg: "#0B0B0E",
          surface: "#14141A",
          card: "#1D1E26",
          border: "#272730",
          text: "#E4E5EC",
          muted: "#7B7C88",
          dim: "#3B3B45",
          signal: "#D4875A",
          "signal-soft": "rgba(212, 135, 90, 0.12)",
          "signal-line": "rgba(212, 135, 90, 0.35)",
          echo: "#3D7A8E",
          "echo-soft": "rgba(61, 122, 142, 0.12)",
          "echo-line": "rgba(61, 122, 142, 0.3)",
        },
      },
      borderRadius: {
        "2xl": "1rem",
        "3xl": "1.25rem",
      },
      animation: {
        "radar-spin": "radar-spin 3s linear infinite",
        "radar-blip": "radar-blip 2s ease-out infinite",
        "signal-pulse": "signal-pulse 1.6s ease-out infinite",
        "fade-away": "fade-away 2.5s ease-out forwards",
        "spectrum-fill": "spectrum-fill 0.6s ease-out forwards",
        "spectrum-scan": "spectrum-scan 1.8s ease-in-out infinite",
        "spectrum-flash": "spectrum-flash 0.5s ease-out",
        "spectrum-bar-glow": "spectrum-bar-glow 2s ease-in-out infinite alternate",
        "slide-up": "slide-up 0.3s ease-out",
        "fade-in": "fade-in 0.2s ease-out",
        "blip-enter": "blip-enter 0.4s ease-out forwards",
        "item-arrive": "item-arrive 0.45s ease-out forwards",
      },
      keyframes: {
        "radar-spin": {
          from: { transform: "rotate(0deg)" },
          to: { transform: "rotate(360deg)" },
        },
        "radar-blip": {
          "0%": { transform: "scale(0)", opacity: "1" },
          "100%": { transform: "scale(3)", opacity: "0" },
        },
        "signal-pulse": {
          "0%, 100%": { opacity: "1" },
          "50%": { opacity: "0.5" },
        },
        "fade-away": {
          from: { opacity: "1" },
          to: { opacity: "0.35" },
        },
        "spectrum-fill": {
          from: { width: "0%" },
          to: { width: "var(--pct)" },
        },
        "spectrum-scan": {
          "0%": { transform: "translateX(-100%)" },
          "100%": { transform: "translateX(100%)" },
        },
        "spectrum-bar-glow": {
          "0%, 100%": { boxShadow: "0 0 3px rgba(212, 135, 90, 0.12)" },
          "50%": { boxShadow: "0 0 10px rgba(212, 135, 90, 0.3), 0 0 20px rgba(212, 135, 90, 0.08)" },
        },
        "spectrum-flash": {
          "0%": { boxShadow: "0 0 0 rgba(212, 135, 90, 0)" },
          "40%": { boxShadow: "0 0 10px rgba(212, 135, 90, 0.25), 0 0 20px rgba(212, 135, 90, 0.1)" },
          "100%": { boxShadow: "0 0 0 rgba(212, 135, 90, 0)" },
        },
        "slide-up": {
          from: { opacity: "0", transform: "translateY(8px)" },
          to: { opacity: "1", transform: "translateY(0)" },
        },
        "fade-in": {
          from: { opacity: "0" },
          to: { opacity: "1" },
        },
        "item-arrive": {
          "0%": { opacity: "0", transform: "translateX(-12px) scale(0.97)" },
          "40%": { opacity: "1", transform: "translateX(0) scale(1.005)", boxShadow: "0 0 12px rgba(212, 135, 90, 0.08)" },
          "100%": { opacity: "1", transform: "translateX(0) scale(1)", boxShadow: "0 0 0 rgba(212, 135, 90, 0)" },
        },
        "blip-enter": {
          "0%": { opacity: "0", transform: "translateX(-8px)" },
          "100%": { opacity: "1", transform: "translateX(0)" },
        },
      },
    },
  },
  plugins: [],
}
