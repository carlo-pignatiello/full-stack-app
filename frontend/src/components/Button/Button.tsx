import { component$, QRL } from '@builder.io/qwik';

export interface ButtonProps {
  label: string;
  type: 'button' | 'submit';
  variant: "primary" | "outlined" | "link";
  size: "sm" | "md";
  onClick$?: QRL<() => void>;
}

export const Button = component$<ButtonProps>(({ label, size, variant, ...props }: ButtonProps) => {

  var text_class = ""
  if (variant === "primary") {
    text_class = "text-zinc-100 bg-gray-900 rounded-full hover:bg-gray-950"
  } else if (variant === "outlined") {
    text_class = "text-gray-900 bg-zinc-100 rounded-full hover:bg-gray-200"
  } else if (variant === "link") {
    text_class = "text-gray-900 font-medium hover:underline hover:font-semibold "
  }

  return (
    <button
      class={
        ["px-4",
          text_class,
          size === "sm" ? "text-sm py-1" : "text-md py-2"
        ]
      }
      {...props}
      >{label}
    </button>
  );
});
