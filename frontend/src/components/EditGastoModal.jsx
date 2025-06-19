import React, { useState } from 'react';

const EditGastoModal = ({ open, onClose, gasto, handleEdit }) => {
  
  const [ monto, setGasto ] = useState(gasto.monto);
  const [ descripcion, setDescripcion ] = useState(gasto.descripcion);
  const [ fecha, setFecha ] = useState(gasto.fecha);
  const [ categoria_id, setCategoriaId ] = useState(gasto.categoria_id);

  if (!open) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-40 flex items-center justify-center z-50">
      <div className="bg-white rounded-lg p-6 w-full max-w-md shadow-lg">
        <h2 className="text-xl font-bold mb-4">Editar Gasto</h2>
        <form className="flex flex-col gap-4">
          <input
            className="border rounded px-3 py-2"
            type="number"
            name="monto"
            placeholder="Monto"
            value={monto}
            onChange={(e) => setGasto(e.target.value)}
          />
          <input
            className="border rounded px-3 py-2"
            type="text"
            name="descripcion"
            placeholder="Descripción"
            value={descripcion}
            onChange={(e) => setDescripcion(e.target.value)}
          />
          <input
            className="border rounded px-3 py-2"
            type="date"
            name="fecha"
            placeholder="Fecha"
            value={fecha}
            onChange={(e) => setFecha(e.target.value)}
          />
          <input
            className="border rounded px-3 py-2"
            type="number"
            name="categoria_id"
            placeholder="Categoría ID"
            value={categoria_id}
            onChange={(e) => setCategoriaId(e.target.value)}
          />
        </form>
        <div className="flex justify-end gap-2 mt-6">
          <button
            className="px-4 py-2 rounded bg-gray-300 hover:bg-gray-400"
            onClick={onClose}
            type="button"
          >
            Cancelar
          </button>
          <button
            className="px-4 py-2 rounded bg-blue-500 text-white hover:bg-blue-600"
            onClick={() => {
              // Aquí podrías manejar la lógica para editar el gasto
              console.log('Gasto editado:', { monto, descripcion, fecha, categoria_id });
              handleEdit(gasto.id, { id: gasto.id , monto, descripcion, fecha, categoria_id });
              onClose();
            }}
            type="button"
          >Guardar</button>
        </div>
      </div>
    </div>
  );
};

export default EditGastoModal;