import React from 'react'

const Mensaje = (props) => {
  return (
    <div className={`rounded-xl px-3 py-2 ${props.isUser ? 'bg-[#1a4558] text-white rounded-tr-none' : 'bg-[#f1f1f1] rounded-tl-none'} break-words`}>{props.mensaje}</div>
  )
}

export default Mensaje