import "../styles/style.css"
import React, { useState } from 'react'


const Cricket = (props) => {
console.log("props" ,props)
  console.log("targert = " , props.target)
  //states are created here inside the function
  const [runs , setRuns] = useState(0);
  const [wickets , setWickets] = useState(0);
  const [target , setTarget] = useState(props.target);
  const [Balls,setCount] = useState(0);
  
    // const handleSix = () =>{
    //     setRuns(runs + 6);
    // }

    // const handleFour = () =>{
    //     setRuns(runs + 4);
    // }

  // const handleOne = () =>{
  //     setRuns(runs + 1);
  // }

  const handleRuns = (run) => {
    if(runs + run >= target)
      alert("Target Chased");
      setRuns(runs + run)
  };

  

    // overs done => "Failed to Chase Target"

  const handleWicket = () =>{

  if(wickets + 1 === 10)
    alert("All Out");
    setWickets(wickets + 1); // it will take some time to update
  }

  const handlecount = (ball) =>{
    setCount(Balls + ball)
  }
  
const overs = Math.floor(Balls / 6);
const ballsInCurrentOver = Balls % 6;
const currentOver = `${overs + 1}.${ballsInCurrentOver}`;
const totalBalls = props.totalOvers * 6
const remainingBalls = totalBalls - Balls
const OversLeft =  `${Math.floor(remainingBalls/6)}.${remainingBalls % 6}`;
  
  

  return (
    <>
        <h1>Scrore : {runs} / {wickets}</h1>
        {
          Balls >= totalBalls ?
          <h2>Failed to chase.</h2>
          :
        <>
        <h2>Current Over :{currentOver}</h2>
        <h2>Overs Left:{OversLeft}</h2>
        <h2> Balls : {Balls}</h2>
    
         </>
         }
        {
            wickets < 10 && runs < target && Balls < totalBalls ?
            <div>
                <button onClick = {()=> {handleRuns(0),handlecount(1);}}> Dot</button>
                <button onClick={() =>{handleRuns(1),handlecount(1);}} >One</button>
                <button onClick = {()=> {handleRuns(2),handlecount(1);}}>Two</button>
                <button onClick = {()=> {handleRuns(3),handlecount(1);}}>Three</button>
                 <button onClick={()=>{handleRuns(4),handlecount(1);}} >Four</button>
                <button onClick={()=>{handleRuns(6),handlecount(1);}} >Six</button>
                <button onClick={() =>{handleWicket(0),handlecount(1);} } >Wicket</button>                                       
            </div>
            :
            <h2>Game Over</h2>
        }


    </>
    
  )
}
     
export default Cricket