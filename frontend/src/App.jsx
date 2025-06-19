import './App.css'
import Chat from './components/Chat'
import EditGastoModal from './components/EditGastoModal'
import Gasto from './components/Gasto'
import { useState } from 'react'

const gastosMock = [
  {
    "id": 1,
    "monto": 1200.50,
    "descripcion": "Compra de supermercado",
    "fecha": "2025-06-15",
    "categoria_id": 3
  },
  {
    "id": 2,
    "monto": 350.00,
    "descripcion": "Pago de internet",
    "fecha": "2025-06-10",
    "categoria_id": 2
  },
  {
    "id": 3,
    "monto": 75.25,
    "descripcion": "Cena en restaurante",
    "fecha": "2025-06-18",
    "categoria_id": 1
  },
  {
    "id": 4,
    "monto": 500.00,
    "descripcion": "Gasolina",
    "fecha": "2025-06-12",
    "categoria_id": 4
  },
  {
    "id": 5,
    "monto": 200.00,
    "descripcion": "Suscripción a streaming",
    "fecha": "2025-06-05",
    "categoria_id": 5
  }
]

// const mockCategorias = [
//   { "id": 1, "nombre": "Alimentación" },
//   { "id": 2, "nombre": "Servicios" },
//   { "id": 3, "nombre": "Supermercado" },
//   { "id": 4, "nombre": "Transporte" },
//   { "id": 5, "nombre": "Entretenimiento" }
// ]

const defaultGasto = {
  "id": 0,
  "monto": 0,
  "descripcion": "", 
  "fecha": new Date().toISOString().split('T')[0], // Formato YYYY-MM-DD
  "categoria_id": 1 // Default category ID
}

function App() {

  const [ gastos, setGastos ] = useState(gastosMock)
  const [ openModal, setOpenModal ] = useState(false)

  const handleOpenModal = () => {
    setOpenModal(true)
  }

  const onCloseModal = () => {
    setOpenModal(false)
  }

  const handleDelete = (id) => {
    console.log("asd")
    setGastos(gastos.filter(gasto => gasto.id !== id));
  }

  const handleEdit = (id, updatedGasto) => {
    setGastos(gastos.map(gasto => (gasto.id === id ? updatedGasto : gasto)));
  }

  const handleAdd = (newGasto) => {
    newGasto.id = gastos.length + 1; // Simple ID generation
    setGastos([...gastos, newGasto]);
  }

  return (
    <div className='flex flex-col min-h-screen'>
      <header className='bg-blue-300 p-4'>
        <h2>Gastos App</h2>
      </header>
      <main className='bg-[#e7ecef] flex-1 p-8'>
        <Chat />
        <table className="min-w-full bg-white rounded-lg shadow">
          <thead>
            <tr>
              <th className="px-4 py-2 text-left">Descripción</th>
              <th className="px-4 py-2 text-left">Valor</th>
              <th className="px-4 py-2 text-left">Categoría</th>
              <th className="px-4 py-2 text-left">Fecha</th>
              <th className="px-4 py-2 text-left">Acciones</th>
            </tr>
          </thead>
          <tbody>
            { gastos.map(gasto => (
              <Gasto id={gasto.id} handleDelete={handleDelete} handleEdit={handleEdit} key={gasto.id} categoria_id={gasto.categoria_id} fecha={gasto.fecha} descripcion={gasto.descripcion} monto={gasto.monto}/>
            )) }
          </tbody>
        </table>
        <button className='px-4 py-2 rounded bg-blue-500 text-white hover:bg-blue-600' onClick={handleOpenModal}>+</button>
        <EditGastoModal open={openModal} onClose={onCloseModal} handleEdit={handleAdd} gasto={defaultGasto}/>
      </main>
      <footer className='bg-blue-300 p-4 text-end'>
        <h2>asd</h2>
      </footer>
    </div >
  )
}

export default App
