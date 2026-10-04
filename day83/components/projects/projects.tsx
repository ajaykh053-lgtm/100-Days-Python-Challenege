import {
  Package,
  ArrowRight,
  LucidePersonStanding,
  NotebookPen,
  Voicemail,
  LucideSignpost,
  Video,
} from "lucide-react";
import type { ComponentType, ReactNode } from "react";
import Image from "next/image";
import Link from "next/link";

import { FadeIn } from "@/components/ui/motion-primitives";

/**
 * Project imagery below is mockup-only. All visuals are sourced from
 * Dribbble and credit belongs to the original creators on dribbble.com.
 * Replace these with your own work before shipping.
 */

type Project = {
  id: string;
  icon: ComponentType<{ className?: string }>;
  iconLabel: string;
  title: string;
  description: string;
  meta: string;
  imageRatio: number;
  image: string;
  imageAlt: string;
};

const PROJECTS: Project[] = [
  {
    id: "BlogPost",
    icon: LucideSignpost,
    iconLabel: "BlogPost",
    title:
      "A modern blog platform with a rich editor, instant publishing, and a reading experience readers actually enjoy.",
    description:
      "I designed and developed a full-stack blog website where authors can draft in markdown, publish in one click, and readers can browse by topic, search posts, and engage through comments.",
    meta: "Full-Stack Developer, 2026",
    imageRatio: 752 / 497,
    image:
      "https://cdn.dribbble.com/userupload/44695858/file/1d27d81393f0fa564ff755bcae423e4a.jpg?resize=1504x1128&vertical=center",
    imageAlt: "Blog Post Website Image",
  },
  {
    id: "bootstrapwebpage",
    icon: Package,
    iconLabel: "Move It",
    title:
      "A responsive landing page that makes booking a move feel simple, friendly, and stress-free.",
    description:
      "I designed and built Move It, a mobile-first Bootstrap website for a moving startup, with a clear hero, service highlights, a testimonial carousel, and quote calls-to-action on every section.",
    meta: "Frontend Developer, 2026",
    imageRatio: 1024 / 768,
    image:
      "https://cdn.dribbble.com/userupload/20306197/file/original-53a7d073839c95a801b8ee47f481a6d4.png?format=webp&resize=400x300&vertical=center",
    imageAlt: "Web page Only Using The Bootstrap.",
  },
  {
    id: "oldprotfolio",
    icon: LucidePersonStanding,
    iconLabel: "Old Portfolio",
    title:
      "A clean, responsive developer portfolio that puts my projects, tech stack, and resume one click away.",
    description:
      "I built a single-page portfolio deployed on Vercel that highlights my full-stack work, links to live projects and GitHub repos, and gives recruiters everything they need to get in touch quickly.",
    meta: "Full-Stack Developer, 2026",
    imageRatio: 1024 / 768,
    image:
      "https://cdn.dribbble.com/userupload/47357856/file/75841fa59f32f05ca6c5ddf02d08dfe6.png?resize=1024x768&vertical=center",
    imageAlt: "My Old Portfolio site",
  },
  {
    id: "VoiceRag",
    icon: Voicemail,
    iconLabel: "Voice Rag",
    title:
      "A voice-first AI assistant that listens in your language and answers from your own knowledge base.",
    description:
      "I built a voice-enabled RAG pipeline that turns speech into text, retrieves relevant context from multilingual datasets, and generates grounded answers, making information accessible through simple conversation.",
    meta: "AI & Full-Stack Developer, 2026",
    imageRatio: 1024 / 768,
    image:
      "https://cdn.dribbble.com/userupload/48539829/file/783a4e35f08529c63e95f8e3b0bef9e2.png?resize=1504x1128&vertical=center",
    imageAlt: "Voice Rag Website",
  },
  {
    id: "top-10-movies",
    icon: Video,
    iconLabel: "Top 10 Movie",
    title:
      "A Flask-powered movie collection site with live search, ratings, and automatic top 10 ranking.",
    description:
      "I developed a CRUD web app with Flask, SQLAlchemy, and WTForms that pulls movie details from an external API, stores them in a database, and ranks films by rating.",
    meta: "Python Full-Stack Developer, 2026",
    imageRatio: 1024 / 768,
    image:
      "https://cdn.dribbble.com/userupload/18886167/file/original-b7134b2699927b376f8917ee9e559b85.png?resize=400x300&vertical=center",
    imageAlt: "Top 10 movies according to me.",
  },
  {
    id: "smartattandacesystem ",
    icon: NotebookPen,
    iconLabel: "Smart Attendance system",
    title:
      "A digital attendance system that replaces paper registers with real-time tracking, secure logins, and one-click reports.",
    description:
      "I designed and built a full-stack attendance platform where attendance is marked and monitored live, access is role-based, and records can be exported as CSV reports automatically.",
    meta: "Full-Stack Developer, 2026",
    imageRatio: 1024 / 768,
    image:
      "https://cdn.dribbble.com/userupload/18073762/file/original-29825fa125f91ec9d45f32873b9f4fb5.jpg?resize=1504x1128&vertical=center",
    imageAlt: "Smart Attendance system for college",
  },
];

export type ProjectsProps = {
  withHeadline?: boolean;
  viewMoreVisible?: boolean;
};

export function Projects({
  withHeadline = false,
  viewMoreVisible = false,
}: ProjectsProps): ReactNode {
  const items = viewMoreVisible ? PROJECTS.slice(0, 4) : PROJECTS;

  return (
    <section className="relative w-full">
      <div className="mx-auto w-full max-w-275 px-6 sm:px-10">
        {withHeadline ? (
          <FadeIn className="flex flex-col items-center gap-5 pt-12 pb-10 text-center sm:pt-20 sm:pb-14">
            <h2 className="font-serif text-[2.5rem] font-medium leading-[1.05] tracking-tight text-foreground md:text-[3rem] lg:text-[3.5rem]">
              My projects
            </h2>
            <p className="max-w-[33ch] text-[18px] leading-[1.45] tracking-tight text-foreground/65 sm:text-[20px]">
              From playful experiments to thoughtful systems, a look at the
              work I&rsquo;m proud to have shipped.
            </p>
          </FadeIn>
        ) : null}

        <div className="columns-1 gap-6 md:columns-2 md:gap-7">
          {items.map((project, index) => (
            <ProjectCard key={project.id} project={project} index={index} />
          ))}
        </div>

        {viewMoreVisible ? (
          <div className="mt-12 flex justify-center sm:mt-16">
            <Link
              href="/projects"
              className="border border-foreground/8 focus-ring group inline-flex cursor-pointer items-center gap-2 rounded-xl bg-background px-5 py-2.5 text-sm font-medium text-foreground transition-colors hover:bg-foreground/5"
            >
              View all projects
              <ArrowRight
                className="h-4 w-4 transition-transform duration-300 group-hover:translate-x-0.5"
                aria-hidden="true"
              />
            </Link>
          </div>
        ) : null}
      </div>
    </section>
  );
}

function ProjectCard({
  project,
  index,
}: {
  project: Project;
  index: number;
}): ReactNode {
  const Icon = project.icon;
  return (
    <FadeIn
      delay={Math.min(index * 0.06, 0.3)}
      className="mb-6 break-inside-avoid md:mb-7"
    >
      <article className="project-card flex cursor-pointer flex-col gap-4 rounded-3xl border border-foreground/8 bg-background p-3 sm:p-3.5">
        <header className="flex items-center gap-2.5 px-1 pt-2">
          <span className="border-foreground/10 inline-flex h-8 w-8 shrink-0 items-center justify-center rounded-lg border bg-background">
            <Icon className="h-3.5 w-3.5 text-foreground" aria-hidden="true" />
          </span>
          <span className="text-sm font-medium tracking-tight text-foreground">
            {project.iconLabel}
          </span>
        </header>

        <div
          className="project-card__image ring-foreground/5 relative w-full overflow-hidden rounded-2xl bg-foreground/5 ring-1"
          style={{ aspectRatio: project.imageRatio }}
        >
          <div className="project-card__image-inner">
            <Image
              src={project.image}
              alt={project.imageAlt}
              fill
              sizes="(min-width: 1024px) 540px, (min-width: 768px) 45vw, 100vw"
              className="object-cover"
              priority={index < 2}
            />
          </div>
        </div>

        <div className="flex flex-col gap-2.5 px-1 pb-1">
          <h3 className="text-[20px] font-medium leading-[1.2] tracking-tight text-foreground sm:text-[22px]">
            {project.title}
          </h3>
          <p className="text-[14px] leading-normal tracking-tight text-foreground/65 sm:text-[15px]">
            {project.description}
          </p>
        </div>

        <p className="px-1 pb-2 text-[12px] tracking-tight text-foreground/50">
          {project.meta}
        </p>
      </article>
    </FadeIn>
  );
}
