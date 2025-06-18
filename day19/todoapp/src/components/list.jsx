import React from 'react'



const list = () => {
    const players = ["Rohit" , "Virat", "Kl rahul"]
  return (
    <div>
        players.map((element,index)=>{
            return <div key = {index}>
                <h1>{}</h1>
            </div>

        })
    </div>
  )
}

export default list