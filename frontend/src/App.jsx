import { useEffect, useState } from 'react'

export default function App() {
  const [pets, setPets] = useState([])
  const [form, setForm] = useState({ name: '', species: '', breed: '', price: '' })

  const loadPets = () => fetch('/api/pets').then(r => r.json()).then(setPets)
  useEffect(() => { loadPets() }, [])

  const handleSubmit = async (e) => {
    e.preventDefault()
    await fetch('/api/pets', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ ...form, price: parseFloat(form.price) }),
    })
    setForm({ name: '', species: '', breed: '', price: '' })
    loadPets()
  }

  const handleDelete = async (id) => {
    await fetch(`/api/pets/${id}`, { method: 'DELETE' })
    loadPets()
  }

  return (
    <div style={{ maxWidth: 640, margin: '40px auto', fontFamily: 'sans-serif' }}>
      <h1>🐾 Pet Shop</h1>

      <form onSubmit={handleSubmit} style={{ display: 'flex', gap: 8, marginBottom: 24 }}>
        <input placeholder="Name" value={form.name} required
          onChange={e => setForm({ ...form, name: e.target.value })} />
        <input placeholder="Species" value={form.species} required
          onChange={e => setForm({ ...form, species: e.target.value })} />
        <input placeholder="Breed" value={form.breed}
          onChange={e => setForm({ ...form, breed: e.target.value })} />
        <input placeholder="Price" type="number" value={form.price} required
          onChange={e => setForm({ ...form, price: e.target.value })} />
        <button type="submit">Add</button>
      </form>

      <table width="100%" cellPadding="8" style={{ borderCollapse: 'collapse' }}>
        <thead>
          <tr style={{ textAlign: 'left', borderBottom: '2px solid #ccc' }}>
            <th>Name</th><th>Species</th><th>Breed</th><th>Price</th><th></th>
          </tr>
        </thead>
        <tbody>
          {pets.map(p => (
            <tr key={p.id} style={{ borderBottom: '1px solid #eee' }}>
              <td>{p.name}</td><td>{p.species}</td><td>{p.breed || '—'}</td>
              <td>${p.price}</td>
              <td><button onClick={() => handleDelete(p.id)}>✕</button></td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}