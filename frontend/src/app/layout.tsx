import type { Metadata } from "next";
import { Fraunces, Manrope } from "next/font/google";

import "../styles/globals.css";

const manrope = Manrope({
  subsets: ["latin"],
  variable: "--font-sans",
});

const fraunces = Fraunces({
  subsets: ["latin"],
  variable: "--font-display",
});

export const metadata: Metadata = {
  title: "Chat App MVP",
  description: "Monorepo-style chat app scaffold with Next.js and FastAPI.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={`${manrope.variable} ${fraunces.variable} min-h-screen bg-sand text-ink`}>
        <div className="pointer-events-none fixed inset-0 bg-[radial-gradient(circle_at_top_left,_rgba(178,76,45,0.18),_transparent_34%),radial-gradient(circle_at_bottom_right,_rgba(65,92,73,0.14),_transparent_30%)]" />
        <div className="relative">{children}</div>
      </body>
    </html>
  );
}

