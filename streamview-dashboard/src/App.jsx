import React, { useState, useMemo } from 'react';
import { 
  LineChart, Line, BarChart, Bar, PieChart, Pie, Cell, 
  XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer 
} from 'recharts';
import Slider from 'rc-slider';
import 'rc-slider/assets/index.css';

// --- DATA MAESTRA (Años 2000 a 2025) ---
const masterEvolucion = [
  { year: '2000', pelicula: 4, serie: 1 }, { year: '2001', pelicula: 5, serie: 2 },
  { year: '2002', pelicula: 5, serie: 3 }, { year: '2003', pelicula: 6, serie: 4 },
  { year: '2004', pelicula: 8, serie: 5 }, { year: '2005', pelicula: 7, serie: 6 },
  { year: '2006', pelicula: 9, serie: 7 }, { year: '2007', pelicula: 10, serie: 12 },
  { year: '2008', pelicula: 11, serie: 15 }, { year: '2009', pelicula: 15, serie: 18 },
  { year: '2010', pelicula: 18, serie: 25 }, { year: '2011', pelicula: 22, serie: 28 },
  { year: '2012', pelicula: 25, serie: 30 }, { year: '2013', pelicula: 28, serie: 34 },
  { year: '2014', pelicula: 32, serie: 38 }, { year: '2015', pelicula: 40, serie: 42 },
  { year: '2016', pelicula: 45, serie: 43 }, { year: '2017', pelicula: 48, serie: 44 },
  { year: '2018', pelicula: 52, serie: 48 }, { year: '2019', pelicula: 50, serie: 47 },
  { year: '2020', pelicula: 42, serie: 30 }, { year: '2021', pelicula: 45, serie: 32 },
  { year: '2022', pelicula: 55, serie: 35 }, { year: '2023', pelicula: 60, serie: 36 },
  { year: '2024', pelicula: 75, serie: 33 }, { year: '2025', pelicula: 20, serie: 13 },
];

const dataGeneros = [
  { name: 'Drama', cantidad: 14776 }, { name: 'Comedia', cantidad: 9110 },
  { name: 'Animación', cantidad: 4070 }, { name: 'Thriller', cantidad: 3769 },
  { name: 'Acción', cantidad: 3239 },
];

const dataPaises = [
  { name: 'EE.UU.', cantidad: 8500 }, { name: 'India', cantidad: 2300 },
  { name: 'Reino Unido', cantidad: 1800 }, { name: 'Japón', cantidad: 1200 },
  { name: 'Corea', cantidad: 900 },
];

const dataAudiencia = [
  { name: 'Adultos (+18)', valor: 45, color: '#E50914' },
  { name: 'Adolescentes', valor: 35, color: '#3b82f6' },
  { name: 'Familiar/Infantil', valor: 20, color: '#22c55e' },
];

function App() {
  const [activeTab, setActiveTab] = useState('Evolución del Catálogo');
  const [yearRange, setYearRange] = useState([2000, 2025]);
  const [format, setFormat] = useState('Ambos');

  const tabs = ['Evolución del Catálogo', 'Top Géneros', 'Países', 'Valoración de la Audiencia'];

  // 🧠 LÓGICA INNOVADORA: Filtrado en tiempo real
  const filteredEvolucion = useMemo(() => {
    return masterEvolucion.filter(item => {
      const y = parseInt(item.year);
      return y >= yearRange[0] && y <= yearRange[1];
    });
  }, [yearRange]);

  // 🧮 KPIs Dinámicos calculados desde los datos filtrados
  const totalPeliculas = useMemo(() => filteredEvolucion.reduce((acc, curr) => acc + curr.pelicula, 0), [filteredEvolucion]);
  const totalSeries = useMemo(() => filteredEvolucion.reduce((acc, curr) => acc + curr.serie, 0), [filteredEvolucion]);
  
  let metricTotal = 0;
  if (format === 'Ambos') metricTotal = totalPeliculas + totalSeries;
  if (format === 'Película') metricTotal = totalPeliculas;
  if (format === 'Serie') metricTotal = totalSeries;

  const pctPeliculas = Math.round((totalPeliculas / (totalPeliculas + totalSeries)) * 100) || 0;
  const pctSeries = 100 - pctPeliculas;

  const renderChart = () => {
    switch(activeTab) {
      case 'Evolución del Catálogo':
        return (
          <ResponsiveContainer width="100%" height="100%">
            <LineChart data={filteredEvolucion} margin={{ top: 5, right: 10, bottom: 20, left: -20 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="#333333" vertical={false} />
              <XAxis dataKey="year" stroke="#808080" tick={{ fill: '#808080', fontSize: 12 }} tickLine={false} axisLine={false} dy={15} />
              <YAxis stroke="#808080" tick={{ fill: '#808080', fontSize: 12 }} tickLine={false} axisLine={false} dx={-10} />
              <Tooltip 
                contentStyle={{ backgroundColor: '#1E1E1E', border: '1px solid #333', borderRadius: '8px', color: '#E5E5E5' }} 
                itemStyle={{ fontWeight: 'bold' }}
              />
              {/* Renderizado condicional de líneas según el formato seleccionado */}
              {(format === 'Ambos' || format === 'Película') && (
                <Line type="monotone" dataKey="pelicula" stroke="#E50914" strokeWidth={3} dot={{ r: 4, fill: '#E50914', strokeWidth: 0 }} activeDot={{ r: 6 }} name="Película" animationDuration={1000} />
              )}
              {(format === 'Ambos' || format === 'Serie') && (
                <Line type="monotone" dataKey="serie" stroke="#3b82f6" strokeWidth={3} dot={{ r: 4, fill: '#3b82f6', strokeWidth: 0 }} activeDot={{ r: 6 }} name="Serie" animationDuration={1000} />
              )}
            </LineChart>
          </ResponsiveContainer>
        );
      case 'Top Géneros':
        return (
          <ResponsiveContainer width="100%" height="100%">
            <BarChart data={dataGeneros} layout="vertical" margin={{ top: 5, right: 30, bottom: 5, left: 30 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="#333333" horizontal={true} vertical={false} />
              <XAxis type="number" stroke="#808080" tick={{ fill: '#808080' }} />
              <YAxis dataKey="name" type="category" stroke="#E5E5E5" tick={{ fill: '#E5E5E5', fontSize: 13, fontWeight: 'bold' }} axisLine={false} tickLine={false} />
              <Tooltip cursor={{ fill: '#333333', opacity: 0.4 }} contentStyle={{ backgroundColor: '#1E1E1E', border: '1px solid #333', borderRadius: '8px' }} />
              <Bar dataKey="cantidad" fill={format === 'Serie' ? '#3b82f6' : '#E50914'} radius={[0, 4, 4, 0]} barSize={25} animationDuration={1000} />
            </BarChart>
          </ResponsiveContainer>
        );
      case 'Países':
        return (
          <ResponsiveContainer width="100%" height="100%">
            <BarChart data={dataPaises} margin={{ top: 20, right: 30, bottom: 20, left: -10 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="#333333" vertical={false} />
              <XAxis dataKey="name" stroke="#808080" tick={{ fill: '#E5E5E5', fontSize: 13 }} tickLine={false} axisLine={false} dy={10} />
              <YAxis stroke="#808080" tick={{ fill: '#808080' }} tickLine={false} axisLine={false} />
              <Tooltip cursor={{ fill: '#333333', opacity: 0.4 }} contentStyle={{ backgroundColor: '#1E1E1E', border: '1px solid #333', borderRadius: '8px' }} />
              <Bar dataKey="cantidad" fill={format === 'Película' ? '#E50914' : '#3b82f6'} radius={[4, 4, 0, 0]} barSize={40} animationDuration={1000} />
            </BarChart>
          </ResponsiveContainer>
        );
      case 'Valoración de la Audiencia':
        return (
          <ResponsiveContainer width="100%" height="100%">
            <PieChart>
              <Pie data={dataAudiencia} innerRadius={90} outerRadius={140} paddingAngle={5} dataKey="valor" stroke="none" animationDuration={1000}>
                {dataAudiencia.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={entry.color} />
                ))}
              </Pie>
              <Tooltip contentStyle={{ backgroundColor: '#1E1E1E', border: '1px solid #333', borderRadius: '8px', color: '#E5E5E5' }} />
            </PieChart>
          </ResponsiveContainer>
        );
      default: return null;
    }
  };

  return (
    <div className="min-h-screen flex bg-[#121212] text-[#E5E5E5] font-sans">
      {/* BARRA LATERAL */}
      <aside className="w-[280px] bg-[#1E1E1E] p-6 border-r border-[#333333] flex flex-col shrink-0">
        <h1 className="text-[#E50914] font-bold text-2xl mb-1 tracking-widest">STREAMVIEW</h1>
        <p className="text-[10px] text-[#E5E5E5] tracking-[0.4em] mb-10 font-bold">ANALYTICS</p>

        <div className="mb-10">
          <p className="text-[10px] text-[#808080] uppercase tracking-wider mb-4 border-b border-[#333333] pb-2">Formato</p>
          <div className="flex items-center gap-4 text-sm">
            {['Ambos', 'Película', 'Serie'].map(opcion => (
              <label key={opcion} className={`flex items-center gap-2 cursor-pointer transition-colors ${format === opcion ? 'text-white font-medium' : 'text-[#808080] hover:text-white'}`}>
                <input type="radio" name="format" checked={format === opcion} onChange={() => setFormat(opcion)} className="accent-[#E50914] w-4 h-4" /> {opcion}
              </label>
            ))}
          </div>
        </div>

        <div className="mb-8">
          <p className="text-[10px] text-[#808080] uppercase tracking-wider mb-4 border-b border-[#333333] pb-2">Período</p>
          <p className="text-sm mb-4 text-[#808080]">Rango de años de lanzamiento</p>
          <div className="flex justify-between text-[#E50914] text-sm mb-3 font-bold">
            <span>{yearRange[0]}</span>
            <span>{yearRange[1]}</span>
          </div>
          <div className="px-1">
            <Slider 
              range 
              min={2000} 
              max={2025} 
              value={yearRange} 
              onChange={setYearRange}
              trackStyle={[{ backgroundColor: '#E50914', height: 4 }]}
              handleStyle={[
                { backgroundColor: '#E50914', borderColor: '#E50914', opacity: 1, marginTop: -5, width: 14, height: 14 },
                { backgroundColor: '#E50914', borderColor: '#E50914', opacity: 1, marginTop: -5, width: 14, height: 14 }
              ]}
              railStyle={{ backgroundColor: '#333333', height: 4 }}
            />
          </div>
        </div>
      </aside>

      {/* PANEL PRINCIPAL */}
      <main className="flex-1 p-8 overflow-x-hidden">
        <header className="mb-8 flex justify-between items-end border-b border-[#333333] pb-4">
          <div>
            <h2 className="text-3xl font-bold mb-2">Panel de Decisiones Estratégicas</h2>
            <p className="text-[#808080] text-sm">Catálogo dinámico · StreamView Analytics</p>
          </div>
          <div className="text-xs text-[#808080] flex flex-col items-end gap-2 font-medium">
            <span>REPORTE · 20 SEP 2026</span>
            <span className="flex items-center gap-2 text-[#22c55e] bg-[#22c55e]/10 px-3 py-1 rounded-full border border-[#22c55e]/20">
              <span className="w-2 h-2 bg-[#22c55e] rounded-full animate-pulse"></span> LIVE
            </span>
          </div>
        </header>

        {/* Tarjetas KPI Inteligentes */}
        <div className="grid grid-cols-4 gap-6 mb-8">
          <div className="bg-[#1E1E1E] p-5 rounded-lg border-t-[3px] border-[#E50914] shadow-md transition-all duration-300">
            <p className="text-[10px] text-[#808080] uppercase tracking-widest mb-2 font-semibold">Títulos {format !== 'Ambos' ? format + 's' : 'Totales'}</p>
            <p className="text-4xl font-bold mb-4">{metricTotal.toLocaleString('es-CL')}</p>
            <div className="w-full bg-[#333333] h-1 mb-3 rounded-full"><div className="bg-[#E50914] w-[100%] h-1 rounded-full"></div></div>
            <p className="text-[11px] text-[#808080]">En el rango seleccionado</p>
          </div>
          
          <div className={`bg-[#1E1E1E] p-5 rounded-lg border-t-[3px] ${format === 'Película' ? 'border-[#E50914]' : format === 'Serie' ? 'border-[#3b82f6]' : 'border-gray-500'} shadow-md transition-all duration-300`}>
            <p className="text-[10px] text-[#808080] uppercase tracking-widest mb-2 font-semibold">Películas vs Series</p>
            <p className="text-3xl font-bold mb-4">{totalPeliculas.toLocaleString('es-CL')} / {totalSeries.toLocaleString('es-CL')}</p>
            <div className="flex w-full h-1 mb-3 rounded-full overflow-hidden">
                <div className="bg-[#E50914] h-1 transition-all duration-500" style={{ width: `${pctPeliculas}%` }}></div>
                <div className="bg-[#3b82f6] h-1 transition-all duration-500" style={{ width: `${pctSeries}%` }}></div>
            </div>
            <p className="text-[11px] text-[#808080]">
              <span className="text-[#E50914] mr-1">●</span>{pctPeliculas}% pelis · <span className="text-[#3b82f6] ml-1 mr-1">●</span>{pctSeries}% series
            </p>
          </div>
          
          <div className="bg-[#1E1E1E] p-5 rounded-lg border-t-[3px] border-[#22c55e] shadow-md">
            <p className="text-[10px] text-[#808080] uppercase tracking-widest mb-2 font-semibold">Rango Analizado</p>
            <p className="text-4xl font-bold mb-4">{yearRange[0]} - {yearRange[1]}</p>
            <div className="w-full bg-[#333333] h-1 mb-3 rounded-full"><div className="bg-[#22c55e] w-[100%] h-1 rounded-full"></div></div>
            <p className="text-[11px] text-[#808080]">{yearRange[1] - yearRange[0] + 1} años en pantalla</p>
          </div>
          
          <div className="bg-[#1E1E1E] p-5 rounded-lg border-t-[3px] border-[#f97316] shadow-md">
            <p className="text-[10px] text-[#808080] uppercase tracking-widest mb-2 font-semibold">Popularidad Mediana</p>
            <p className="text-4xl font-bold mb-4">23.2</p>
            <p className="text-[11px] text-[#22c55e] mt-7 font-medium">↑ Dinámica de interacciones activa</p>
          </div>
        </div>

        {/* Zona de Gráficos */}
        <div className="flex gap-6 h-[480px]">
          <div className="bg-[#1E1E1E] p-6 rounded-lg flex-1 shadow-md flex flex-col">
            <div className="flex gap-8 border-b border-[#333333] mb-8 text-sm">
              {tabs.map(tab => (
                <span 
                  key={tab} 
                  onClick={() => setActiveTab(tab)}
                  className={`pb-3 cursor-pointer transition-all ${activeTab === tab ? 'border-b-2 border-[#E50914] text-[#E5E5E5] font-bold' : 'text-[#808080] hover:text-[#E5E5E5]'}`}
                >
                  {tab}
                </span>
              ))}
            </div>
            <div className="flex-1 w-full relative">
              {renderChart()}
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;