import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'

export default function Login() {
    return (
        <div className='flex flex-col align-center justify-between rounded-lg p-4 w-96 bg-slate-200 h-80'>
            <div className='flex flex-col align-center p-4 mb-18'>
                <div className='flex justify-center p-4'>
                    <Input placeholder='Username' className='w-60 h-8'></Input>
                </div>
                <div className='flex justify-center p-4'>
                    <Input placeholder='Password' className='w-60 h-8'></Input>
                </div>
            </div>
            <div className='flex justify-center p-4'>
                <Button variant="link" size="sm">Registra</Button>
                <Button size="sm">Accedi</Button>
            </div>
        </div>
    )
}
