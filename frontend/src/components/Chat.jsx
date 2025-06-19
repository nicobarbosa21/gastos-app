import Mensaje from "./Mensaje"
import { useState } from "react"
import { IoMdSend } from "react-icons/io";

const Chat = () => {

  const [ historial, setHistorial ] = useState(["Hola"])
  const [ mensaje, setMensaje ] = useState("")
  const [ isLoading, setIsLoading ] = useState(false)

  const mandarMensaje = (mensaje) => {
    setHistorial([...historial, mensaje, "Cargando..."])
    setMensaje("")
    setIsLoading(true)

    setTimeout(() => {
    // Simulate bot response after 3 seconds
    setHistorial(prev => {
      // Remove the last "Cargando..." and add the bot response
      const newHistorial = [...prev];
      newHistorial.pop();
      return [...newHistorial, "Respuesta del bot"];
    });
    setIsLoading(false);
  }, 3000);
    // Post con el mensaje al backend
    // setmensaje con la respuesta del bot
  }

  return (
    <div className="border-1 w-64 bg-[#274c77] rounded-lg">
      <ul className="flex flex-col gap-2 p-2">
        { historial.map((mensaje, index) => (
          <li key={index}>
            <Mensaje key={index} mensaje={mensaje} isUser={index % 2 != 0}/>
          </li>
        ))}
      </ul>
      <div className="p-2 border-t-1">
        <div className="flex gap-2 bg-[#6096ba] text-white placeholder-gray-50 rounded-xl">
          <input 
            type="text" 
            placeholder="Escribe un mensaje" 
            className="flex-1 min-w-0 px-2" 
            value={mensaje} 
            onChange={e => setMensaje(e.target.value)}/>
          <button 
            className={`py-2 px-3 rounded-xl hover:cursor-pointer text-[#274c77] ${isLoading && 'bg-gray-[#a3cef1] hover:bg-gray-[#a3cef1]'}`} 
            onClick={() => mandarMensaje(mensaje)} 
            disabled={isLoading || mensaje.trim() === ""}
          >
            <IoMdSend/>
          </button>
        </div>
      </div>
    </div>
  )
}

export default Chat