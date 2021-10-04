
            const userlist = JSON.parse(document.getElementById('userlist').textContent);
            const deg = JSON.parse(document.getElementById('deg').textContent);
            console.log(typeof(userlist))
            let colorsXXX = [
                "#ee1c24",
                "#3cb878",
                "#f6989d",
                "#00aef0",
                "#f26522",
                "#000000",
                "#e70697",
                "#fff200",
                "#f6989d",
                "#ee1c24",
                "#3cb878",
                "#f26522",
                "#a186be",
                "#fff200",
                "#00aef0",
                "#ee1c24",
                "#f6989d",
                "#f26522",
                "#3cb878",
                "#000000",
                "#a186be",
                "#fff200",
                "#00aef0",
                "#ffffff",
                "#ee1c24",
                "#3cb878",
                "#f6989d",
                "#00aef0",
                "#f26522",
                "#000000",
                "#e70697",
                "#fff200",
                "#f6989d",
                "#ee1c24",
                "#3cb878",
                "#f26522",
                "#a186be",
                "#fff200",
                "#00aef0",
                "#ee1c24",
                "#f6989d",
                "#f26522",
                "#3cb878",
                "#000000",
                "#a186be",
                "#fff200",
                "#00aef0",
                "#ffffff",
                "#ee1c24",
                "#3cb878",
                "#f6989d",
                "#00aef0",
                "#f26522",
                "#000000",
                "#e70697",
                "#fff200",
                "#f6989d",
                "#ee1c24",
                "#3cb878",
                "#f26522",
                "#a186be",
                "#fff200",
                "#00aef0",
                "#ee1c24",
                "#f6989d",
                "#f26522",
                "#3cb878",
                "#000000",
                "#a186be",
                "#fff200",
                "#00aef0",
                "#ffffff",
                "#ee1c24",
                "#3cb878",
                "#f6989d",
                "#00aef0",
                "#f26522",
                "#000000",
                "#e70697",
                "#fff200",
                "#f6989d",
                "#ee1c24",
                "#3cb878",
                "#f26522",
                "#a186be",
                "#fff200",
                "#00aef0",
                "#ee1c24",
                "#f6989d",
                "#f26522",
                "#3cb878",
                "#000000",
                "#a186be",
                "#fff200",
                "#00aef0",
                "#ffffff",
                
              ]
              let colorsYYY = [
                
                "black",
                "black",
                "black",
                "black",
                "white",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "white",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "white",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "white",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "white",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "white",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "white",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "white",
                "black",
                "black",
                "black",
                "black",
                
              ]

            let segments = []
            if(userlist.length == 2){
                for(i = 0; i < 5; i++){

                    userlist.map((e,key)=>{
                        // var randomColor = Math.floor(Math.random()*16777215).toString(16);
                        console.log(e,key)
                        console.log(colorsXXX[key])
                        obj = {'fillStyle' : colorsXXX[key], 'text' : e, 'textFillStyle' : colorsYYY[key]}
                        segments.push(obj)
                    })

                }
            } else if (userlist.length == 3){
                for(i = 0; i < 4; i++){

                    userlist.map((e,key)=>{
                        // var randomColor = Math.floor(Math.random()*16777215).toString(16);
                        console.log(e,key)
                        console.log(colorsXXX[key])
                        obj = {'fillStyle' : colorsXXX[key], 'text' : e, 'textFillStyle' : colorsYYY[key]}
                        segments.push(obj)
                    })

                }
            } else if (userlist.length == 4){
                for(i = 0; i < 3; i++){

                    userlist.map((e,key)=>{
                        // var randomColor = Math.floor(Math.random()*16777215).toString(16);
                        console.log(e,key)
                        console.log(colorsXXX[key])
                        obj = {'fillStyle' : colorsXXX[key], 'text' : e, 'textFillStyle' : colorsYYY[key]}
                        segments.push(obj)
                    })

                }
            } else if (userlist.length > 4 && userlist.length < 10){
                for(i = 0; i < 2; i++){

                    userlist.map((e,key)=>{
                        // var randomColor = Math.floor(Math.random()*16777215).toString(16);
                        console.log(e,key)
                        console.log(colorsXXX[key])
                        obj = {'fillStyle' : colorsXXX[key], 'text' : e, 'textFillStyle' : colorsYYY[key]}
                        segments.push(obj)
                    })

                }
            } else {
                

                userlist.map((e,key)=>{
                    // var randomColor = Math.floor(Math.random()*16777215).toString(16);
                    console.log(e,key)
                    console.log(colorsXXX[key])
                    obj = {'fillStyle' : colorsXXX[key], 'text' : e, 'textFillStyle' : colorsYYY[key]}
                    segments.push(obj)
                })

                
            }
            
            
            // Create new wheel object specifying the parameters at creation time.
            let theWheel = new Winwheel({
                'outerRadius'     : 212,        // Set outer radius so wheel fits inside the background.
                'innerRadius'     : 75,         // Make wheel hollow so segments don't go all way to center.
                'textFontSize'    : 16,         // Set default font size for the segments.
                'textOrientation' : 'vertical', // Make text vertial so goes down from the outside of wheel.
                'textAlignment'   : 'outer',    // Align text to outside of wheel.
                'numSegments'     : segments.length,         // Specify number of segments.
                'segments'        :   segments,          // Define segments including colour and text.
                'animation' :           // Specify the animation to use.
                {
                    'type'     : 'spinToStop',
                    'duration' : 10,    // Duration in seconds.
                    'spins'    : 3,     // Default number of complete spins.
                    'callbackFinished' : alertPrize,
                    'callbackSound'    : playSound,   // Function to call when the tick sound is to be triggered.
                    'soundTrigger'     : 'pin'        // Specify pins are to trigger the sound, the other option is 'segment'.
                },
                'pins' :				// Turn pins on.
                {
                    'number'     : segments.length,
                    'fillStyle'  : 'yellow',
                    'outerRadius': 4,
                }
            });

            // Loads the tick audio sound in to an audio object.
            let audio = new Audio('../../../static/wheelspin/game/media/tick.mp3');

            // This function is called when the sound is to be played.
            function playSound()
            {
                // Stop and rewind the sound if it already happens to be playing.
                audio.pause();
                audio.currentTime = 0;

                // Play the sound.
                audio.play();
            }

            // Vars used by the code in this page to do power controls.
            let wheelPower    = 0;
            let wheelSpinning = false;

            // -------------------------------------------------------
            // Function to handle the onClick on the power buttons.
            // -------------------------------------------------------
            /*function powerSelected(powerLevel)
            {
                // Ensure that power can't be changed while wheel is spinning.
                if (wheelSpinning == false) {
                    // Reset all to grey incase this is not the first time the user has selected the power.
                    document.getElementById('pw1').className = "";
                    document.getElementById('pw2').className = "";
                    document.getElementById('pw3').className = "";

                    // Now light up all cells below-and-including the one selected by changing the class.
                    if (powerLevel >= 1) {
                        document.getElementById('pw1').className = "pw1";
                    }

                    if (powerLevel >= 2) {
                        document.getElementById('pw2').className = "pw2";
                    }

                    if (powerLevel >= 3) {
                        document.getElementById('pw3').className = "pw3";
                    }

                    // Set wheelPower var used when spin button is clicked.
                    

                    // Light up the spin button by changing it's source image and adding a clickable class to it.
                    //document.getElementById('spin_button').src = "spin_on.png";
                    
                }
            }*/
            wheelPower = 3;
            document.getElementById('spin_button').className = "clickable";

            // -------------------------------------------------------
            // Click handler for spin button.
            // -------------------------------------------------------
            function startSpin()
            {
                // Ensure that spinning can't be clicked again while already running.
                if (wheelSpinning == false) {
                    // Based on the power level selected adjust the number of spins for the wheel, the more times is has
                    // to rotate with the duration of the animation the quicker the wheel spins.
                    if (wheelPower == 1) {
                        theWheel.animation.spins = 3;
                    } else if (wheelPower == 2) {
                        theWheel.animation.spins = 6;
                    } else if (wheelPower == 3) {
                        theWheel.animation.spins = 500;
                    }

                    // Disable the spin button so can't click again while wheel is spinning.
                    //document.getElementById('spin_button').src       = "spin_off.png";
                    document.getElementById('spin_button').className = "";

                    // Begin the spin animation by calling startAnimation on the wheel object.
                    theWheel.startAnimation();

                    // Set to true so that power can't be changed and spin button re-enabled during
                    // the current animation. The user will have to reset before spinning again.
                    wheelSpinning = false;
                }
            }

            // -------------------------------------------------------
            // Function for reset button.
            // -------------------------------------------------------
            function resetWheel()
            {
                theWheel.stopAnimation(false);  // Stop the animation, false as param so does not call callback function.
                theWheel.rotationAngle = 0;     // Re-set the wheel angle to 0 degrees.
                theWheel.draw();                // Call draw to render changes to the wheel.

                document.getElementById('pw1').className = "";  // Remove all colours from the power level indicators.
                document.getElementById('pw2').className = "";
                document.getElementById('pw3').className = "";

                wheelSpinning = false;          // Reset to false to power buttons and spin can be clicked again.
            }

            // -------------------------------------------------------
            // Called when the spin animation has finished by the callback feature of the wheel because I specified callback in the parameters.
            // -------------------------------------------------------
            function alertPrize(indicatedSegment)
            {
                // console.log("SJKDHJSAHGDJKSAHJDKHSAJKDHSAJKDHJSAKHDJKSAHDJSAH")
                // // Just alert to the user what happened.
                // // In a real project probably want to do something more interesting than this with the result.
                if (indicatedSegment.text == 'LOOSE TURN') {
                //     console.log("CCCCC1")
                //     setTimeout(
                //         function() {
                //             let fzf = document.querySelector('#rme')
                //             fzf.innerHTML = `
                //             <div style="background:black;display:flex;justify-content:center;">
                //                 <div>
                //                     <h1>The Winner is ${indicatedSegment.text}</h1>
                //                     <a style="display:flex;justify-content:center;">
                //                         <button class="btn btn-primary my-4">Please Wait Redirecting</button>
                //                     </a>
                //                 </div>
                //             </div>
                //             `
                //         }, 1000);
                    // alert('Sorry but you loose a turn.');
                    
                } else if (indicatedSegment.text == 'BANKRUPT') {
                    // console.log("CCCCC2")
                    // setTimeout(
                    //     function() {
                    //         let fzf = document.querySelector('#rme')
                    //         fzf.innerHTML = `
                    //         <div style="background:black;display:flex;justify-content:center;">
                    //             <div>
                    //                 <h1>The Winner is ${indicatedSegment.text}</h1>
                    //                 <a style="display:flex;justify-content:center;">
                    //                     <button class="btn btn-primary my-4">Please Wait Redirecting</button>
                    //                 </a>
                    //             </div>
                    //         </div>
                    //         `
                    //     }, 1000);
                    // alert('Oh no, you have gone BANKRUPT!');
                } else {
                    // console.log("CCCCC3")
                    // // alert("You have won " + indicatedSegment.text);
                    // setTimeout(
                    //     function() {
                    //         let fzf = document.querySelector('#rme')
                    //         fzf.innerHTML = `
                    //         <div style="background:black;display:flex;justify-content:center;">
                    //             <div>
                    //                 <h1>The Winner is ${indicatedSegment.text}</h1>
                    //                 <a style="display:flex;justify-content:center;">
                    //                     <button class="btn btn-primary my-4">Please Wait Redirecting</button>
                    //                 </a>
                    //             </div>
                    //         </div>
                    //         `
                    //     }, 1000);
            
                    
                }
            }

