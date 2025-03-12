text = [
    'Your one-stop-shop for all your electrical and robotics needs.', 
    'Transforming Ideas into Reality - Where Innovation Meets Accessibility',
    'Empowering Innovators, Connecting Circuits',
    'Shop Now and Join the Vibrant Community of Circuit Enthusiasts!'
]

var typed = new Typed('#element', {
    strings: text,
    typeSpeed: 25,
    backspeed: 50,
    loop: true
  });
      // Simulate click event on 'Enter' key press
  document.addEventListener('keydown', function(event) {
  if (event.key === 'Enter') {
      document.getElementById('hiddenButton').click();
  }
  });