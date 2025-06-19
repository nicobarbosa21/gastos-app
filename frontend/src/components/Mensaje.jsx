import React from 'react'

const Mensaje = (props) => {
  return (
    <div className={`rounded-xl px-3 py-2 ${props.isUser ? 'bg-[#6096ba]' : 'bg-[#e7ecef]'} break-words`}>{props.mensaje}</div>
  )
}

export default Mensaje