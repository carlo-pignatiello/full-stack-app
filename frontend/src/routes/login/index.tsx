import { component$, $ } from '@builder.io/qwik';
import { useNavigate } from '@builder.io/qwik-city';
import { Button } from '~/components/Button/Button';

export default component$(() => {
  const nav = useNavigate();
  const onLogin = $(() => {
    console.log("Hello")
    // nav("/signup")
  });
  return (
    <Button label="Login" size="sm" variant="primary" onClick$={() => console.log("hello")}></Button>
  );
});
