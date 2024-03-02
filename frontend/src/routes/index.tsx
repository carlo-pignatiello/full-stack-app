import { component$, $ } from "@builder.io/qwik";
import type { DocumentHead, RequestEvent } from "@builder.io/qwik-city";
import Login from "./login";

export const onGet = async ({ cookie, redirect }: RequestEvent) => {
  throw redirect(302, '/login/');
};

export const head: DocumentHead = {
  title: "Welcome to Qwik",
  meta: [
    {
      name: "description",
      content: "Qwik site description",
    },
  ],
};
