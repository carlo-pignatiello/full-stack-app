import { RequestHandler, routeLoader$, useNavigate, RequestEvent } from '@builder.io/qwik-city';
import { component$ } from '@builder.io/qwik';
import {
  type InitialValues,
  minLength,
  required,
  useForm,
  valiForm$,
  formAction$
} from '@modular-forms/qwik';

import * as v from 'valibot';
import { TextInput } from '~/components/Input/TextInput';
import { Button } from '~/components/Button/Button';

const LoginSchema = v.object({
  username: v.string([
    v.minLength(1, 'Please enter your email.'),
  ]),
  password: v.string([
    v.minLength(1, 'Please enter your password.'),
    v.minLength(4, 'You password must have 4 characters or more.'),
  ]),
});

type LoginForm = v.Input<typeof LoginSchema>;

export const useFormLoader = routeLoader$<InitialValues<LoginForm>>(() => {
  return {
    username: '',
    password: '',
  };
});

export const useFormAction = formAction$<LoginForm>(async (values) => {
  const param = {
    username: values.username,
    password: values.password
  }
  const response = await fetch("http://localhost:8000/signin",
    {
      method: "POST",
      body: JSON.stringify(param),
      headers: {
        "Content-type": "application/json; charset=UTF-8"
      }
    }
  );
  const res = await response.json();
  console.log(res)
}, valiForm$(LoginSchema));


export default component$(() => {
  const [loginForm, { Form, Field }] = useForm<LoginForm>({
    loader: useFormLoader(),
    action: useFormAction(),
    validate: valiForm$(LoginSchema)
  });
  const nav = useNavigate()

  return (
    <div class="flex items-center w-96 rounded-md justify-center m-4 p-4 bg-gray-200">
      <Form>
        <Field
          name="username"
        >
          {(field, props) => (
            <>
              <TextInput
                {...props}
                type="username"
                label="Username"
                value={field.value}
                error={field.error}
                required
              />
            </>
          )}
        </Field>
        <Field
          name="password"
        >
          {(field, props) => (
            <>
              <TextInput
                {...props}
                type="password"
                label="Password"
                value={field.value}
                error={field.error}
                required
              />
            </>
          )}
        </Field>
        <div class='px-2 flex flex-row items-center justify-between'>
          <Button type='button' size='md' variant='link' label='Signup' onClick$={() => nav('/signup/')}></Button>
          <Button type="submit" size='sm' variant='primary' label='Login'></Button>
        </div>
      </Form>
    </div>
  );
});
