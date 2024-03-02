import { component$, type QRL } from '@builder.io/qwik';

type TextInputProps = {
  name: string;
  type: 'text' | 'username' | 'email' | 'password' | 'url' | 'date';
  label?: string;
  placeholder?: string;
  value: string | undefined;
  error: string;
  required?: boolean;
  ref: QRL<(element: HTMLInputElement) => void>;
  onInput$: (event: Event, element: HTMLInputElement) => void;
  onChange$: (event: Event, element: HTMLInputElement) => void;
//   onBlur$: (event: Event, element: HTMLInputElement) => void;
};

export const TextInput = component$(
  ({ label, error, ...props }: TextInputProps) => {
    const { name, required } = props;
    return (
      <div class="flex flex-col p-2 mb-2">
        {label && (
          <label for={name}>
            {label} {required && <span>*</span>}
          </label>
        )}
        <input
          class="focus:outline-none ring-1 ring-gray-400 rounded-md focus:ring-2 focus:ring-gray-600 p-1"
          {...props}
          id={name}
          aria-invalid={!!error}
          aria-errormessage={`${name}-error`}
        />
        {error && <div id={`${name}-error`}>{error}</div>}
      </div>
    );
  }
);
