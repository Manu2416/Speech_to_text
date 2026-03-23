const textarea = document.getElementById('texto_a_traducir');
const resultadoBox = document.getElementById('resultado-box');
const idiomaDetectado = document.getElementById('idioma-detectado');
const textoTraducido = document.getElementById('texto-traducido');
let timeout = null;

textarea.addEventListener('input', () => {
    
    timeout = setTimeout(async () => {
        const texto = textarea.value.trim();
        if (!texto) {
            resultadoBox.style.display = 'none';
            return;
        }

        const formData = new FormData();
        formData.append('texto_a_traducir', texto);
        formData.append('idioma_destino', document.getElementById('idioma_destino').value);

        try {
            const res = await fetch('/procesar', {
                method: 'POST',
                body: formData
            });

            const data = await res.json();

            resultadoBox.style.display = 'block';
            idiomaDetectado.innerText = data.detectado;
            textoTraducido.innerText = data.traducido;

        } catch (error) {
            console.error("Error al traducir:", error);
        }
    }, 500); // espera 500ms después de que el usuario deje de escribir
});

// 🎤 SPEECH TO TEXT
document.getElementById('btn-voz').onclick = async () => {
    const res = await fetch('/speech-to-text');
    const data = await res.json();

    // metemos el texto en el textarea
    document.getElementById('texto_a_traducir').value = data.texto.replace("Recognized: ", "");
};

// 🔊 TEXT TO SPEECH
document.getElementById('btn-audio').onclick = async () => {
    const texto = document.getElementById('texto-traducido').innerText;

    if (!texto) {
        alert("Primero traduce algo");
        return;
    }

    const formData = new FormData();
    formData.append("texto", texto);

    const res = await fetch('/text-to-speech', {
        method: 'POST',
        body: formData
    });

    const data = await res.json();

    const audioPlayer = document.getElementById('audio-player');
    audioPlayer.style.display = 'block';
    audioPlayer.play();
};