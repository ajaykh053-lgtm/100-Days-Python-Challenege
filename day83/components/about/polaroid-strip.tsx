"use client";

import { motion, useMotionValue, useSpring } from "motion/react";
import Image from "next/image";
import {
  useRef,
  useSyncExternalStore,
  type PointerEvent as ReactPointerEvent,
  type ReactNode,
} from "react";

type Polaroid = {
  id: string;
  rotate: number;
  src: string;
  alt: string;
  caption: string;
};

const PHOTOS: Polaroid[] = [
  { id: "a", rotate: -8, src: "/photos/robin.jpg", alt: "Robin", caption: "Demon Child" },
  { id: "b", rotate: 6, src: "/photos/Nami.jpg", alt: "Nami", caption: "Cat Burglar" },
  { id: "c", rotate: -4, src: "/photos/Usopp.jpg", alt: "Usopp", caption: "Warrior of the Sea" },
  { id: "d", rotate: 7, src: "/photos/Luffy.jpg", alt: "Luffy", caption: "King of the Pirates" },
  { id: "e", rotate: -6, src: "/photos/Zoro.jpg", alt: "Zoro", caption: "World's Greatest Swordsman" },
  { id: "f", rotate: 5, src: "/photos/Sanji.jpg", alt: "Sanji", caption: "World's Best Cook" },
];

const EASE = [0.22, 1, 0.36, 1] as const;

function PolaroidCard({
  photo,
  index,
}: {
  photo: Polaroid;
  index: number;
}): ReactNode {
  const ref = useRef<HTMLDivElement | null>(null);
  const mx = useMotionValue(0);
  const my = useMotionValue(0);
  const sx = useSpring(mx, { stiffness: 220, damping: 18, mass: 0.6 });
  const sy = useSpring(my, { stiffness: 220, damping: 18, mass: 0.6 });

  const handleMove = (e: ReactPointerEvent<HTMLDivElement>): void => {
    const el = ref.current;
    if (!el) return;
    const rect = el.getBoundingClientRect();
    const cx = rect.left + rect.width / 2;
    const cy = rect.top + rect.height / 2;
    const dx = e.clientX - cx;
    const dy = e.clientY - cy;
    const max = 18;
    const k = 0.25;
    mx.set(Math.max(-max, Math.min(max, dx * k)));
    my.set(Math.max(-max, Math.min(max, dy * k)));
  };

  const handleLeave = (): void => {
    mx.set(0);
    my.set(0);
  };

  return (
    // Outer element: entrance animation only
    <motion.div
      initial={{ opacity: 0, y: -120, filter: "blur(18px)" }}
      animate={{ opacity: 1, y: 0, filter: "blur(0px)" }}
      transition={{
        duration: 0.9,
        delay: 0.05 + index * 0.08,
        ease: EASE,
      }}
      className="shrink-0"
    >
      {/* Inner element: pointer-follow spring + rotation */}
      <motion.div
        ref={ref}
        onPointerMove={handleMove}
        onPointerLeave={handleLeave}
        style={{ x: sx, y: sy, rotate: photo.rotate }}
        className="relative aspect-[3/4.6] w-[clamp(6rem,11vw,9rem)] overflow-hidden rounded-2xl border-6 border-neutral-300/40 bg-white p-1.5 dark:border-white/15 dark:bg-neutral-900"
      >
        <div className="flex h-full w-full flex-col">
          <div className="relative flex-1 overflow-hidden rounded-lg">
            <Image
              src={photo.src}
              alt={photo.alt}
              fill
              sizes="(min-width: 640px) 9rem, 6rem"
              className="object-cover"
              draggable={false}
            />
          </div>
          <p className="line-clamp-2 min-h-[2.5em] pt-1.5 text-center font-mono text-[10px] leading-tight text-neutral-600 dark:text-neutral-300 sm:text-xs">
            {photo.caption}
          </p>
        </div>
      </motion.div>
    </motion.div>
  );
}

export function PolaroidStrip(): ReactNode {
  const mounted = useSyncExternalStore(
    () => () => { },
    () => true,
    () => false
  );

  if (!mounted) {
    return <div aria-hidden="true" className="h-[clamp(8rem,15vw,12rem)] w-full" />;
  }

  return (
    <div className="flex w-full flex-wrap items-start justify-center gap-1 px-4 sm:gap-1.5 sm:px-8">
      {PHOTOS.map((photo, i) => (
        <PolaroidCard key={photo.id} photo={photo} index={i} />
      ))}
    </div>
  );
}