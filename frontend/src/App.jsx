import './App.css'
import Chat from './components/chat/Chat'
import TablaGastos from './components/tablaGastos/TablaGastos'

function App() {
  return (
    <div className='flex flex-col min-h-screen'>
      <header className='bg-[#1a4558] text-white p-4 text-center'>
        <h1 className='text-2xl font-bold'>Gastos App</h1>
      </header>
      <main className='bg-[#e7ecef] flex-1 p-4 px-40'>
        <div className='flex flex-col items-center'>
          <h2 className='text-xl mb-2 font-bold'>Gastos por categoria</h2>
          <div className='w-[40vw] h-80 bg-gray-400'></div>
        </div>
        <div className='mt-4 flex flex-col items-center'>
          <h2 className='text-xl mb-2 font-bold'>Lista de Gastos</h2>
          <TablaGastos />
        </div>
        <Chat />
      </main>
      <footer className='bg-[#e7ecef] p-2 text-end'>
        <p>Gastos App made by</p>
      </footer>
    </div >
  )
}

export default App
