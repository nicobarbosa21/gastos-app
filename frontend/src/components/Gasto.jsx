import React from 'react'
import EditGastoModal from './EditGastoModal'

const Gasto = (props) => {

  const [openModal, setOpenModal] = React.useState(false)

  const handleOpenModal = () => {
    setOpenModal(true)
  }

  const onCloseModal = () => {
    setOpenModal(false)
  }

  const gasto = {
    id: props.id,
    monto: props.monto,
    descripcion: props.descripcion,
    fecha: props.fecha,
    categoria_id: props.categoria_id
  }

  return (
    <tr>
      <td className="px-4 py-2">{props.descripcion}</td>
      <td className="px-4 py-2">${props.monto}</td>
      <td className="px-4 py-2">{props.categoria_id}</td>
      <td className="px-4 py-2">{props.fecha}</td>
      <td className="px-4 py-2 flex gap-2">
        <button className="bg-blue-500 text-white px-3 py-1 rounded" onClick={handleOpenModal}>Editar</button>
        <button className="bg-red-500 text-white px-3 py-1 rounded" onClick={() => props.handleDelete(props.id)}>Eliminar</button>
      </td>
      <EditGastoModal open={openModal} gasto={gasto} onClose={onCloseModal} handleEdit={props.handleEdit}/>
    </tr>
  )
}

export default Gasto