import { ButtonHTMLAttributes } from "react";

export function Button({
  className = "",
  ...props
}: ButtonHTMLAttributes<HTMLButtonElement>) {
  return (
    <button
      className={`rounded-md bg-brand px-4 py-2 text-white hover:bg-brand-dark disabled:opacity-50 ${className}`}
      {...props}
    />
  );
}
