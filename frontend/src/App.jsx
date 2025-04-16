import { useState } from 'react'
import './App.css'
import axios from 'axios'

function App() {
  const [file, setFile] = useState(null)
  const [filter, setFilter] = useState('')
  const [resultUrl, setResultUrl] = useState(null)

  const handleUpload = async (e) => {
    e.preventDefault()

    const formData = new FormData()
    formData.append('image', file)
    formData.append('filter', filter)

    try {
      const response = await axios.post('http://127.0.0.1:5000/filter', formData, {
        responseType: 'blob',
      })

      const imageBlob = new Blob([response.data], {type: 'image/jpeg'})
      const imageUrl = URL.createObjectURL(imageBlob)
      setResultUrl(imageUrl)
    } catch(err) {
      console.error('Upload failed: ', err)
    }
  }

  return (
    <div className="app">
      <h2>🖼️ Image Filter App</h2>
      <form onSubmit={handleUpload}>
        <input type="file" onChange={(e) => setFile(e.target.files[0])} required />
        <select onChange={(e) => setFilter(e.target.value)} required>
          <option value="">Select filter</option>
          <option value="grayscale">Grayscale</option>
          <option value="blur">Blur</option>
          <option value="edge">Edge Detection</option>
        </select>
        <button type="submit">Apply</button>
      </form>

      {resultUrl && (
        <>
        <h3>Filtered Image:</h3>
        <img src={resultUrl} alt="Filtered" style={{maxWidth: '400px'}} />
        <br />
        <a href={resultUrl} download="filtered.jpg">Download Image</a>
        </>
      )}
    </div>
  )
}

export default App