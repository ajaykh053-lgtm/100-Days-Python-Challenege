import { Education } from "@/components/about/education";
import { Experience } from "@/components/about/experience";
import { PolaroidStrip } from "@/components/about/polaroid-strip";
import { Skills } from "@/components/about/skills";
import { Stack } from "@/components/about/stack";
import { ContactCard } from "@/components/contact/contact-card";
import { FadeIn } from "@/components/ui/motion-primitives";
import { createMetadata } from "@/lib/metadata";
import type { Metadata } from "next";
import type { ReactNode } from "react";

export const metadata: Metadata = createMetadata({
  title: "About",
  description: "About me, background, and how to get in touch.",
  path: "/about",
});

export default function AboutPage(): ReactNode {
  return (
    <main id="main-content" className="flex flex-1 flex-col">
      <section className="mx-auto w-full max-w-312 pt-40 sm:pt-56">
        <PolaroidStrip />
      </section>

      <section className="mx-auto w-full max-w-160 px-6 pt-20 pb-16 sm:px-10 sm:pt-28 sm:pb-24">
        <FadeIn delay={0.5}>
          <div className="rounded-4xl border border-foreground/5 bg-foreground/1.5 p-8 sm:p-12 dark:bg-foreground/3">
            <h1 className="font-serif text-[1.75rem] font-medium tracking-tight text-foreground sm:text-[2rem]">
              Hello! I&rsquo;m <span className="border-b border-foreground/30 pb-0.5">Ajay</span>.
            </h1>
            <div className="mt-8 space-y-6 text-[17px] leading-[1.7] tracking-tight text-foreground/75 sm:text-[18px]">
              <p>
                A <strong className="font-semibold text-foreground">Python full-stack developer</strong> and computer science student who loves building things that actually work. I enjoy turning ideas into complete products, from <strong className="font-semibold text-foreground">database design</strong> and <strong className="font-semibold text-foreground">backend logic</strong> to clean, responsive interfaces people can use right away.
              </p>
              <p>
                I started with the fundamentals (C, C++, and <strong className="font-semibold text-foreground">data structures and algorithms</strong>) and then found my real spark in Python. Automating small tasks led to web scraping and bots, and that curiosity grew into full-stack apps, real-time systems, and <strong className="font-semibold text-foreground">AI-powered tools</strong> like a multilingual voice RAG pipeline. For me, building is the best way to learn, and every project is a chance to understand how something works under the hood.
              </p>
              <p>
                Currently in my third year of Computer Science Engineering, I&rsquo;m sharpening my DSA and backend skills while shipping projects across web, automation, and AI. I&rsquo;m open to <strong className="font-semibold text-foreground">freelance work and internship opportunities</strong> where I can build reliable software and keep growing as an engineer.
              </p>
            </div>
          </div>
        </FadeIn>
      </section>

      <section className="mx-auto w-full max-w-160 px-6 pb-20 sm:px-10 sm:pb-28">
        <FadeIn delay={0.1}>
          <div className="flex flex-col gap-10">
            <Experience />
            <Education />
            <Skills />
            <Stack />
          </div>
        </FadeIn>
      </section>

      <ContactCard />
      <div className="h-12 sm:h-16" />
    </main>
  );
}
