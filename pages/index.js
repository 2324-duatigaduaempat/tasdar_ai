import Link from 'next/link';

export default function Home() {
  return (
    <main>
      <h1>Selamat Datang ke TAS.DAR</h1>
      <p>UI ini sedang dibina semula dalam Next.js.</p>

      <Link href="/chat">
        <button style={{
          padding: '10px 20px',
          marginTop: '20px',
          fontSize: '16px',
          backgroundColor: '#5e60ce',
          color: 'white',
          border: 'none',
          borderRadius: '6px',
          cursor: 'pointer'
        }}>
          Masuk ke Chatboard GPT
        </button>
      </Link>
    </main>
  );
}
