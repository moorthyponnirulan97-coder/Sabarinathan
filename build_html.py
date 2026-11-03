import json
import os

with open(r'C:\Users\PS 4\.gemini\antigravity\scratch\kpi_dashboard\kpi_data_full.json', 'r', encoding='utf-8') as f:
    raw_data = json.load(f)

json_str = json.dumps(raw_data)

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>H-Series Assembly & Test Operations — Executive KPI Dashboard</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    :root {{
      --bg-main: #0b0f19;
      --card-bg: #111827;
      --card-border: #1f2937;
      --card-hover: #1e293b;
      --text-main: #f3f4f6;
      --text-muted: #9ca3af;
      --primary: #3b82f6;
      --accent: #10b981;
      --warning: #f59e0b;
      --danger: #ef4444;
      --purple: #8b5cf6;
      --cyan: #06b6d4;
    }}
    body {{
      background-color: var(--bg-main);
      color: var(--text-main);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    }}
    .custom-scrollbar::-webkit-scrollbar {{
      width: 6px;
      height: 6px;
    }}
    .custom-scrollbar::-webkit-scrollbar-track {{
      background: #111827;
    }}
    .custom-scrollbar::-webkit-scrollbar-thumb {{
      background: #374151;
      border-radius: 3px;
    }}
    .custom-scrollbar::-webkit-scrollbar-thumb:hover {{
      background: #4b5563;
    }}
    .glass-card {{
      background: rgba(17, 24, 39, 0.85);
      backdrop-filter: blur(8px);
      border: 1px solid rgba(55, 65, 81, 0.6);
    }}
    .nav-tab.active {{
      background: #2563eb;
      color: #ffffff;
      box-shadow: 0 4px 14px 0 rgba(37, 99, 235, 0.39);
    }}
    .badge-critical {{
      background: rgba(239, 68, 68, 0.2);
      color: #f87171;
      border: 1px solid rgba(239, 68, 68, 0.4);
    }}
    .badge-vital {{
      background: rgba(245, 158, 11, 0.2);
      color: #fbbf24;
      border: 1px solid rgba(245, 158, 11, 0.4);
    }}
    .badge-success {{
      background: rgba(16, 185, 129, 0.2);
      color: #34d399;
      border: 1px solid rgba(16, 185, 129, 0.4);
    }}
    .badge-blue {{
      background: rgba(59, 130, 246, 0.2);
      color: #60a5fa;
      border: 1px solid rgba(59, 130, 246, 0.4);
    }}
  </style>
</head>
<body class="min-h-screen p-4 md:p-6 lg:p-8 antialiased custom-scrollbar">

  <!-- TOP HEADER -->
  <header class="mb-6 pb-6 border-b border-gray-800">
    <div class="flex flex-col xl:flex-row xl:items-center xl:justify-between gap-4">
      <div>
        <div class="flex items-center gap-3">
          <span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-semibold bg-blue-900/50 text-blue-400 border border-blue-700">
            FY 2026-27 (H1) Production & Maintenance
          </span>
          <span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-semibold bg-emerald-900/50 text-emerald-400 border border-emerald-700">
            <span class="w-2 h-2 rounded-full bg-emerald-400 mr-1.5 animate-pulse"></span>
            Plant Uptime: 99.05%
          </span>
          <span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-semibold bg-purple-900/50 text-purple-400 border border-purple-700">
            H-SERIES ENGINE
          </span>
        </div>
        <h1 class="text-2xl md:text-3xl font-extrabold tracking-tight mt-2 text-white">
          H-Series Assembly & Test Cell Operations Dashboard
        </h1>
        <p class="text-sm text-gray-400 mt-1">
          Unified Manufacturing Performance, Breakdown Analytics & Machine Reliability Intelligence (April 01 – October 14, 2026)
        </p>
      </div>

      <!-- Quick Actions / Filters -->
      <div class="flex flex-wrap items-center gap-3">
        <div class="bg-gray-900/80 p-1.5 rounded-lg border border-gray-800 flex items-center gap-2">
          <label class="text-xs text-gray-400 px-2 font-medium">Shop Filter:</label>
          <select id="globalShopFilter" onchange="applyGlobalFilter()" class="bg-gray-800 text-xs text-white px-3 py-1.5 rounded border border-gray-700 focus:outline-none focus:border-blue-500">
            <option value="ALL">All Shops (Shop 2 & Shop 5)</option>
            <option value="Shop 2">Shop 2 (Line 2 EA & TB)</option>
            <option value="Shop 5">Shop 5 (Line 1 EA & TB)</option>
          </select>
        </div>
        <button onclick="exportBreakdownCSV()" class="px-3.5 py-1.5 bg-gray-800 hover:bg-gray-700 text-xs font-medium text-gray-200 rounded-lg border border-gray-700 flex items-center gap-1.5 transition">
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
          Export CSV Log
        </button>
      </div>
    </div>

    <!-- PRIMARY KPI CARDS -->
    <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3.5 mt-6">
      
      <!-- Total Assembly Output -->
      <div class="glass-card rounded-xl p-4 relative overflow-hidden">
        <div class="text-xs text-gray-400 uppercase tracking-wider font-semibold">Assembly Output</div>
        <div class="flex items-baseline gap-2 mt-2">
          <span class="text-2xl font-black text-white" id="kpiAssemblyActual">40,553</span>
          <span class="text-xs text-gray-400">/ 54,783</span>
        </div>
        <div class="mt-2 text-xs font-medium flex items-center justify-between">
          <span class="text-amber-400 font-bold" id="kpiAssemblyRate">74.0% Plan</span>
          <span class="text-gray-400 text-[11px]">Loss: -14,230</span>
        </div>
        <div class="w-full bg-gray-800 h-1.5 rounded-full mt-2.5 overflow-hidden">
          <div class="bg-amber-500 h-full rounded-full" style="width: 74.0%"></div>
        </div>
      </div>

      <!-- Test Bed Tested -->
      <div class="glass-card rounded-xl p-4 relative overflow-hidden">
        <div class="text-xs text-gray-400 uppercase tracking-wider font-semibold">Test Cell Throughput</div>
        <div class="flex items-baseline gap-2 mt-2">
          <span class="text-2xl font-black text-white" id="kpiTestedTested">43,829</span>
          <span class="text-xs text-gray-400">Engines</span>
        </div>
        <div class="mt-2 text-xs font-medium flex items-center justify-between">
          <span class="text-emerald-400 font-bold" id="kpiPassedCount">42,412 Passed</span>
          <span class="text-gray-400 text-[11px]">17 Test Beds</span>
        </div>
        <div class="w-full bg-gray-800 h-1.5 rounded-full mt-2.5 overflow-hidden">
          <div class="bg-emerald-500 h-full rounded-full" style="width: 96.8%"></div>
        </div>
      </div>

      <!-- Quality Pass Rate -->
      <div class="glass-card rounded-xl p-4 relative overflow-hidden">
        <div class="text-xs text-gray-400 uppercase tracking-wider font-semibold">First-Time Quality</div>
        <div class="flex items-baseline gap-2 mt-2">
          <span class="text-2xl font-black text-emerald-400" id="kpiQualityRate">96.77%</span>
          <span class="text-xs text-emerald-500">FTT</span>
        </div>
        <div class="mt-2 text-xs font-medium flex items-center justify-between">
          <span class="text-red-400 font-semibold">1,417 Retests</span>
          <span class="text-gray-400 text-[11px]">3.23% Rej Rate</span>
        </div>
        <div class="w-full bg-gray-800 h-1.5 rounded-full mt-2.5 overflow-hidden">
          <div class="bg-emerald-400 h-full rounded-full" style="width: 96.77%"></div>
        </div>
      </div>

      <!-- Breakdown Losses -->
      <div class="glass-card rounded-xl p-4 relative overflow-hidden">
        <div class="text-xs text-gray-400 uppercase tracking-wider font-semibold">Production BD Loss</div>
        <div class="flex items-baseline gap-2 mt-2">
          <span class="text-2xl font-black text-rose-400" id="kpiBDLoss">1,008</span>
          <span class="text-xs text-rose-300">Engines</span>
        </div>
        <div class="mt-2 text-xs font-medium flex items-center justify-between">
          <span class="text-gray-300 font-semibold">731 Incidents</span>
          <span class="text-rose-400 text-[11px]">1.38 / Event</span>
        </div>
        <div class="w-full bg-gray-800 h-1.5 rounded-full mt-2.5 overflow-hidden">
          <div class="bg-rose-500 h-full rounded-full" style="width: 82%"></div>
        </div>
      </div>

      <!-- Machine Downtime -->
      <div class="glass-card rounded-xl p-4 relative overflow-hidden">
        <div class="text-xs text-gray-400 uppercase tracking-wider font-semibold">Total Downtime</div>
        <div class="flex items-baseline gap-2 mt-2">
          <span class="text-2xl font-black text-amber-300" id="kpiDowntimeHours">212.0</span>
          <span class="text-xs text-gray-400">Hours</span>
        </div>
        <div class="mt-2 text-xs font-medium flex items-center justify-between">
          <span class="text-gray-300">12,723 Mins</span>
          <span class="text-amber-400 text-[11px]">Shop 5: 76%</span>
        </div>
        <div class="w-full bg-gray-800 h-1.5 rounded-full mt-2.5 overflow-hidden">
          <div class="bg-amber-400 h-full rounded-full" style="width: 76%"></div>
        </div>
      </div>

      <!-- MTTR -->
      <div class="glass-card rounded-xl p-4 relative overflow-hidden">
        <div class="text-xs text-gray-400 uppercase tracking-wider font-semibold">Mean Time To Repair</div>
        <div class="flex items-baseline gap-2 mt-2">
          <span class="text-2xl font-black text-cyan-400" id="kpiMTTR">17.4</span>
          <span class="text-xs text-cyan-300">Mins / BD</span>
        </div>
        <div class="mt-2 text-xs font-medium flex items-center justify-between">
          <span class="text-gray-400">Shop 2: 7.3m</span>
          <span class="text-cyan-400 text-[11px]">Shop 5: 23.0m</span>
        </div>
        <div class="w-full bg-gray-800 h-1.5 rounded-full mt-2.5 overflow-hidden">
          <div class="bg-cyan-500 h-full rounded-full" style="width: 65%"></div>
        </div>
      </div>

    </div>
  </header>

  <!-- NAVIGATION TABS -->
  <div class="flex flex-wrap gap-2 mb-6">
    <button onclick="switchTab('overview')" id="tabBtn-overview" class="nav-tab active px-4 py-2 rounded-lg text-xs md:text-sm font-semibold transition bg-gray-800 hover:bg-gray-700 text-gray-300">
      Executive Cockpit
    </button>
    <button onclick="switchTab('machines')" id="tabBtn-machines" class="nav-tab px-4 py-2 rounded-lg text-xs md:text-sm font-semibold transition bg-gray-800 hover:bg-gray-700 text-gray-300">
      Machine Breakdown Deep Dive (Top 20)
    </button>
    <button onclick="switchTab('testcells')" id="tabBtn-testcells" class="nav-tab px-4 py-2 rounded-lg text-xs md:text-sm font-semibold transition bg-gray-800 hover:bg-gray-700 text-gray-300">
      Test Cell Performance (17 Cells)
    </button>
    <button onclick="switchTab('subsystems')" id="tabBtn-subsystems" class="nav-tab px-4 py-2 rounded-lg text-xs md:text-sm font-semibold transition bg-gray-800 hover:bg-gray-700 text-gray-300">
      Subsystem & Root Cause Pareto
    </button>
    <button onclick="switchTab('shifts')" id="tabBtn-shifts" class="nav-tab px-4 py-2 rounded-lg text-xs md:text-sm font-semibold transition bg-gray-800 hover:bg-gray-700 text-gray-300">
      Shift & Monthly Dynamics
    </button>
    <button onclick="switchTab('explorer')" id="tabBtn-explorer" class="nav-tab px-4 py-2 rounded-lg text-xs md:text-sm font-semibold transition bg-gray-800 hover:bg-gray-700 text-gray-300">
      Incident Log Explorer (731 Records)
    </button>
    <button onclick="switchTab('actions')" id="tabBtn-actions" class="nav-tab px-4 py-2 rounded-lg text-xs md:text-sm font-semibold transition bg-gray-800 hover:bg-gray-700 text-gray-300">
      Engineering Action Matrix
    </button>
  </div>

  <!-- ================= TAB 1: EXECUTIVE COCKPIT ================= -->
  <div id="tabContent-overview" class="tab-pane space-y-6">

    <!-- Comparative Shop Performance Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
      
      <!-- Shop 2 EA -->
      <div class="glass-card rounded-xl p-5 border-l-4 border-blue-500">
        <div class="flex items-center justify-between">
          <span class="text-xs font-bold text-blue-400 uppercase tracking-wider">Shop 2 Assembly (L2EA)</span>
          <span class="text-xs px-2 py-0.5 rounded bg-blue-900/60 text-blue-300 border border-blue-700">98.51% Uptime</span>
        </div>
        <div class="mt-3 flex items-baseline justify-between">
          <div>
            <div class="text-2xl font-black text-white">22,064</div>
            <div class="text-xs text-gray-400">Planned: 30,453 engines</div>
          </div>
          <div class="text-right">
            <span class="text-lg font-bold text-amber-400">72.5%</span>
            <div class="text-xs text-gray-400">Compliance</div>
          </div>
        </div>
        <div class="mt-4 pt-3 border-t border-gray-800 grid grid-cols-2 gap-2 text-xs">
          <div>
            <span class="text-gray-400">Breakdowns:</span>
            <span class="font-bold text-white ml-1">225</span>
          </div>
          <div>
            <span class="text-gray-400">Engines Lost:</span>
            <span class="font-bold text-rose-400 ml-1">382</span>
          </div>
          <div>
            <span class="text-gray-400">Downtime:</span>
            <span class="font-bold text-amber-300 ml-1">27.3 Hrs</span>
          </div>
          <div>
            <span class="text-gray-400">MTTR:</span>
            <span class="font-bold text-cyan-300 ml-1">7.3 Min</span>
          </div>
        </div>
      </div>

      <!-- Shop 2 TB -->
      <div class="glass-card rounded-xl p-5 border-l-4 border-emerald-500">
        <div class="flex items-center justify-between">
          <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider">Shop 2 Test Bed (L2TB)</span>
          <span class="text-xs px-2 py-0.5 rounded bg-emerald-900/60 text-emerald-300 border border-emerald-700">99.74% Uptime</span>
        </div>
        <div class="mt-3 flex items-baseline justify-between">
          <div>
            <div class="text-2xl font-black text-white">20,077</div>
            <div class="text-xs text-gray-400">Tested: 20,513 engines</div>
          </div>
          <div class="text-right">
            <span class="text-lg font-bold text-emerald-400">97.87%</span>
            <div class="text-xs text-gray-400">FTT Pass</div>
          </div>
        </div>
        <div class="mt-4 pt-3 border-t border-gray-800 grid grid-cols-2 gap-2 text-xs">
          <div>
            <span class="text-gray-400">Breakdowns:</span>
            <span class="font-bold text-white ml-1">86</span>
          </div>
          <div>
            <span class="text-gray-400">Engines Lost:</span>
            <span class="font-bold text-rose-400 ml-1">114.5</span>
          </div>
          <div>
            <span class="text-gray-400">Downtime:</span>
            <span class="font-bold text-amber-300 ml-1">23.7 Hrs</span>
          </div>
          <div>
            <span class="text-gray-400">MTTR:</span>
            <span class="font-bold text-cyan-300 ml-1">16.5 Min</span>
          </div>
        </div>
      </div>

      <!-- Shop 5 EA -->
      <div class="glass-card rounded-xl p-5 border-l-4 border-purple-500">
        <div class="flex items-center justify-between">
          <span class="text-xs font-bold text-purple-400 uppercase tracking-wider">Shop 5 Assembly (L1EA)</span>
          <span class="text-xs px-2 py-0.5 rounded bg-purple-900/60 text-purple-300 border border-purple-700">98.51% Uptime</span>
        </div>
        <div class="mt-3 flex items-baseline justify-between">
          <div>
            <div class="text-2xl font-black text-white">18,489</div>
            <div class="text-xs text-gray-400">Planned: 24,330 engines</div>
          </div>
          <div class="text-right">
            <span class="text-lg font-bold text-amber-400">76.0%</span>
            <div class="text-xs text-gray-400">Compliance</div>
          </div>
        </div>
        <div class="mt-4 pt-3 border-t border-gray-800 grid grid-cols-2 gap-2 text-xs">
          <div>
            <span class="text-gray-400">Breakdowns:</span>
            <span class="font-bold text-white ml-1">181</span>
          </div>
          <div>
            <span class="text-gray-400">Engines Lost:</span>
            <span class="font-bold text-rose-400 ml-1">263</span>
          </div>
          <div>
            <span class="text-gray-400">Downtime:</span>
            <span class="font-bold text-amber-300 ml-1">25.1 Hrs</span>
          </div>
          <div>
            <span class="text-gray-400">MTTR:</span>
            <span class="font-bold text-cyan-300 ml-1">8.3 Min</span>
          </div>
        </div>
      </div>

      <!-- Shop 5 TB -->
      <div class="glass-card rounded-xl p-5 border-l-4 border-rose-500">
        <div class="flex items-center justify-between">
          <span class="text-xs font-bold text-rose-400 uppercase tracking-wider">Shop 5 Test Bed (L1TB)</span>
          <span class="text-xs px-2 py-0.5 rounded bg-rose-900/60 text-rose-300 border border-rose-700">99.45% Uptime</span>
        </div>
        <div class="mt-3 flex items-baseline justify-between">
          <div>
            <div class="text-2xl font-black text-white">22,335</div>
            <div class="text-xs text-gray-400">Tested: 23,316 engines</div>
          </div>
          <div class="text-right">
            <span class="text-lg font-bold text-emerald-400">95.79%</span>
            <div class="text-xs text-gray-400">FTT Pass</div>
          </div>
        </div>
        <div class="mt-4 pt-3 border-t border-gray-800 grid grid-cols-2 gap-2 text-xs">
          <div>
            <span class="text-gray-400">Breakdowns:</span>
            <span class="font-bold text-white ml-1">239</span>
          </div>
          <div>
            <span class="text-gray-400">Engines Lost:</span>
            <span class="font-bold text-rose-400 ml-1">248.5</span>
          </div>
          <div>
            <span class="text-gray-400">Downtime:</span>
            <span class="font-bold text-rose-400 ml-1 font-mono">136.0 Hrs</span>
          </div>
          <div>
            <span class="text-gray-400">MTTR:</span>
            <span class="font-bold text-rose-300 ml-1 font-mono">34.1 Min</span>
          </div>
        </div>
      </div>

    </div>

    <!-- MAIN COCKPIT CHARTS -->
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
      
      <!-- Chart 1: Monthly Production Trend -->
      <div class="lg:col-span-2 glass-card rounded-xl p-5">
        <div class="flex items-center justify-between mb-4">
          <div>
            <h3 class="text-base font-bold text-white">Monthly Engine Assembly Production vs Target</h3>
            <p class="text-xs text-gray-400">Comparison of Manned Capacity vs Passed Output across Shop 2 and Shop 5</p>
          </div>
          <div class="flex items-center gap-3 text-xs">
            <span class="flex items-center gap-1.5"><span class="w-3 h-3 rounded bg-blue-500"></span> Manned Plan</span>
            <span class="flex items-center gap-1.5"><span class="w-3 h-3 rounded bg-emerald-500"></span> Actual Output</span>
          </div>
        </div>
        <div id="monthlyChartContainer" class="h-64 w-full"></div>
      </div>

      <!-- Chart 2: Shift Distribution -->
      <div class="glass-card rounded-xl p-5">
        <h3 class="text-base font-bold text-white mb-1">Breakdown Losses by Shift</h3>
        <p class="text-xs text-gray-400 mb-4">Shift II generates 56.7% of all plant production losses</p>
        
        <div id="shiftDonutContainer" class="h-44 w-full flex items-center justify-center"></div>

        <div class="space-y-2 mt-2 pt-2 border-t border-gray-800 text-xs">
          <div class="flex items-center justify-between p-1.5 rounded bg-gray-800/40">
            <span class="flex items-center gap-2"><span class="w-2.5 h-2.5 rounded-full bg-rose-500"></span> Shift II</span>
            <span class="font-bold text-rose-400">572.0 Loss (56.7%)</span>
            <span class="text-gray-400">132.1 Hrs DT</span>
          </div>
          <div class="flex items-center justify-between p-1.5 rounded bg-gray-800/40">
            <span class="flex items-center gap-2"><span class="w-2.5 h-2.5 rounded-full bg-amber-500"></span> Shift III</span>
            <span class="font-bold text-amber-400">419.5 Loss (41.6%)</span>
            <span class="text-gray-400">75.7 Hrs DT</span>
          </div>
          <div class="flex items-center justify-between p-1.5 rounded bg-gray-800/40">
            <span class="flex items-center gap-2"><span class="w-2.5 h-2.5 rounded-full bg-blue-500"></span> Shift I</span>
            <span class="font-bold text-blue-400">16.5 Loss (1.6%)</span>
            <span class="text-gray-400">4.2 Hrs DT</span>
          </div>
        </div>
      </div>

    </div>

    <!-- Top 5 Bottleneck Callout & Critical Insights -->
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
      
      <!-- Top 5 Loss Impact Machines -->
      <div class="glass-card rounded-xl p-5">
        <div class="flex items-center justify-between mb-3">
          <h3 class="text-base font-bold text-white">Top Critical Machine Losses (Pareto)</h3>
          <span class="text-xs text-rose-400 font-semibold">Responsible for 54% of All Production Loss</span>
        </div>
        <div class="space-y-3" id="top5LossList"></div>
      </div>

      <!-- Key Tactical Insights & Diagnostics -->
      <div class="glass-card rounded-xl p-5">
        <h3 class="text-base font-bold text-white mb-3">Executive Operational Insights</h3>
        <div class="space-y-3.5 text-xs text-gray-300">
          <div class="p-3 rounded-lg bg-blue-950/40 border border-blue-800/50 flex gap-3">
            <div class="text-blue-400 font-bold text-base">01</div>
            <div>
              <strong class="text-white block font-semibold">The Long Block Conveyor (LM03925) is the Primary Flow Disruptor</strong>
              With 74 breakdown events and 83 engine losses, frequent station RFID read timeouts and buffer shunting errors constantly interrupt Shop 2 throughput.
            </div>
          </div>
          <div class="p-3 rounded-lg bg-rose-950/40 border border-rose-800/50 flex gap-3">
            <div class="text-rose-400 font-bold text-base">02</div>
            <div>
              <strong class="text-white block font-semibold">Test Bed 5 (LA10025) Accumulates 35.3 Hours of Downtime Alone</strong>
              TB505 in Shop 5 suffers chronic cooling tower water pressure dips, DDC communication failures, and air in fuel lines requiring manual bleed-downs.
            </div>
          </div>
          <div class="p-3 rounded-lg bg-amber-950/40 border border-amber-800/50 flex gap-3">
            <div class="text-amber-400 font-bold text-base">03</div>
            <div>
              <strong class="text-white block font-semibold">P15 CNG Test Bed (PA640001) First-Time Pass Rate Drops to 84.97%</strong>
              While diesel beds consistently pass 96–98% of engines, the P15 CNG cell rejected 239 units out of 1,590 tested, signaling a sensor calibration and tuning opportunity.
            </div>
          </div>
          <div class="p-3 rounded-lg bg-emerald-950/40 border border-emerald-800/50 flex gap-3">
            <div class="text-emerald-400 font-bold text-base">04</div>
            <div>
              <strong class="text-white block font-semibold">Shift II Represents High Operational Fragility</strong>
              Shift II logs 431 breakdowns and 572 lost units. 62% of plant downtime hits during peak Shift II operations, where quick 'bit resets' mask deeper preventative maintenance needs.
            </div>
          </div>
        </div>
      </div>

    </div>

  </div>

  <!-- ================= TAB 2: MACHINE BREAKDOWN DEEP DIVE ================= -->
  <div id="tabContent-machines" class="tab-pane hidden space-y-6">
    <div class="glass-card rounded-xl p-5">
      <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4 mb-4">
        <div>
          <h3 class="text-lg font-bold text-white">Top 20 Critical Machines by Production Loss & Downtime</h3>
          <p class="text-xs text-gray-400">Detailed reliability ranking across Line 1 & Line 2 equipment (All VITAL assets)</p>
        </div>
        <div class="flex items-center gap-2">
          <input type="text" id="machineSearchInput" onkeyup="filterMachineTable()" placeholder="Search machine, asset ID, or line..." class="bg-gray-900 border border-gray-700 text-xs text-white px-3 py-1.5 rounded-lg focus:outline-none focus:border-blue-500 w-64">
        </div>
      </div>

      <!-- Machine Table -->
      <div class="overflow-x-auto">
        <table class="w-full text-left text-xs text-gray-300">
          <thead class="text-[11px] uppercase tracking-wider bg-gray-900/90 text-gray-400 border-b border-gray-800">
            <tr>
              <th class="p-3 font-semibold">Rank</th>
              <th class="p-3 font-semibold">Asset ID</th>
              <th class="p-3 font-semibold">Machine Description</th>
              <th class="p-3 font-semibold">Line / Shop</th>
              <th class="p-3 font-semibold text-center">Criticality</th>
              <th class="p-3 font-semibold text-right">Breakdowns</th>
              <th class="p-3 font-semibold text-right text-rose-400">Engine Loss (Nos)</th>
              <th class="p-3 font-semibold text-right text-amber-300">Downtime (Hours)</th>
              <th class="p-3 font-semibold text-right">MTTR (Mins)</th>
              <th class="p-3 font-semibold text-center">Action</th>
            </tr>
          </thead>
          <tbody id="machineTableBody" class="divide-y divide-gray-800/60 font-mono text-xs">
          </tbody>
        </table>
      </div>
    </div>
  </div>

  <!-- ================= TAB 3: TEST CELL OPERATIONS ================= -->
  <div id="tabContent-testcells" class="tab-pane hidden space-y-6">
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
      
      <!-- Summary stats -->
      <div class="glass-card rounded-xl p-5 lg:col-span-1">
        <h3 class="text-base font-bold text-white mb-2">Test Cell Benchmarking</h3>
        <p class="text-xs text-gray-400 mb-4">Comparative evaluation across 17 Dynomerk, Diesel, and CNG test cells</p>
        
        <div class="space-y-3 text-xs">
          <div class="p-3 rounded-lg bg-gray-800/40 border border-gray-700/50">
            <div class="text-gray-400">Shop 2 Dynomerk (TB201-204)</div>
            <div class="text-lg font-bold text-white mt-1">20,513 Tested | 97.87% Pass</div>
            <div class="text-[11px] text-gray-400 mt-1">Total Downtime: 23.7 Hours across 86 breakdowns</div>
          </div>
          <div class="p-3 rounded-lg bg-gray-800/40 border border-gray-700/50">
            <div class="text-gray-400">Shop 5 Diesel (TB501-508)</div>
            <div class="text-lg font-bold text-white mt-1">18,716 Tested | 96.86% Pass</div>
            <div class="text-[11px] text-rose-400 mt-1 font-semibold">Total Downtime: 114.7 Hours (TB505 & TB501 dominate)</div>
          </div>
          <div class="p-3 rounded-lg bg-gray-800/40 border border-gray-700/50">
            <div class="text-gray-400">Shop 5 CNG Test Beds (CNG 1-3 & P15)</div>
            <div class="text-lg font-bold text-white mt-1">4,620 Tested | 91.56% Pass</div>
            <div class="text-[11px] text-amber-400 mt-1 font-semibold">P15 CNG pass rate lagging at 84.97% (239 retests)</div>
          </div>
        </div>

        <div class="mt-4 p-3 rounded-lg bg-blue-950/40 border border-blue-900 text-xs text-blue-200">
          <span class="font-bold">Key Insight:</span> While Shop 2 has only 4 high-speed cells, they achieve higher throughput per cell (avg 5,128/cell) than Shop 5 (avg 2,339/cell) due to faster cycle indexing and dedicated fuel conditioning loops.
        </div>
      </div>

      <!-- Test Cells Table -->
      <div class="glass-card rounded-xl p-5 lg:col-span-2">
        <h3 class="text-base font-bold text-white mb-3">All 17 Engine Test Cells Performance Matrix</h3>
        <div class="overflow-x-auto">
          <table class="w-full text-left text-xs">
            <thead class="text-[11px] uppercase tracking-wider bg-gray-900/90 text-gray-400 border-b border-gray-800 font-sans">
              <tr>
                <th class="p-2.5 font-semibold">Asset ID</th>
                <th class="p-2.5 font-semibold">Test Cell</th>
                <th class="p-2.5 font-semibold">Line</th>
                <th class="p-2.5 font-semibold text-right">Tested</th>
                <th class="p-2.5 font-semibold text-right">Passed</th>
                <th class="p-2.5 font-semibold text-right">Retests</th>
                <th class="p-2.5 font-semibold text-right text-emerald-400">FTT Pass %</th>
                <th class="p-2.5 font-semibold text-right text-rose-400">BD Losses</th>
                <th class="p-2.5 font-semibold text-right text-amber-300">Downtime (H)</th>
              </tr>
            </thead>
            <tbody id="testCellTableBody" class="divide-y divide-gray-800/60 font-mono text-xs">
            </tbody>
          </table>
        </div>
      </div>

    </div>
  </div>

  <!-- ================= TAB 4: SUBSYSTEM & ROOT CAUSE PARETO ================= -->
  <div id="tabContent-subsystems" class="tab-pane hidden space-y-6">
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
      
      <!-- Subsystem Pareto List -->
      <div class="glass-card rounded-xl p-5">
        <h3 class="text-base font-bold text-white mb-1">Subsystem Breakdown Pareto (Engine Losses)</h3>
        <p class="text-xs text-gray-400 mb-4">Fastening Tools, Material Handling & Fuel Systems account for 52% of total disruption</p>
        <div id="subsystemList" class="space-y-3"></div>
      </div>

      <!-- Recurring Failure Modes -->
      <div class="glass-card rounded-xl p-5">
        <h3 class="text-base font-bold text-white mb-1">Top Recurring Failure Modes & Root Causes</h3>
        <p class="text-xs text-gray-400 mb-4">Frequent mechanisms diagnosed during incident maintenance</p>
        
        <div class="space-y-3 text-xs" id="abnormalityList"></div>
      </div>

    </div>
  </div>

  <!-- ================= TAB 5: SHIFT & MONTHLY DYNAMICS ================= -->
  <div id="tabContent-shifts" class="tab-pane hidden space-y-6">
    
    <!-- Shift Breakdown Cards -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-5">
      
      <!-- Shift I -->
      <div class="glass-card rounded-xl p-5 border-t-4 border-blue-500">
        <div class="flex items-center justify-between">
          <h4 class="text-base font-bold text-white">Shift I (Morning Setup)</h4>
          <span class="badge-blue text-xs px-2 py-0.5 rounded font-mono font-bold">1.6% Loss</span>
        </div>
        <p class="text-xs text-gray-400 mt-1">Light maintenance, warmup & CNG ramp-up</p>
        <div class="mt-4 space-y-2 text-xs">
          <div class="flex justify-between py-1 border-b border-gray-800">
            <span class="text-gray-400">Assembly Manned vs Actual:</span>
            <span class="font-bold text-white">2,299 / 2,748 (83.7%)</span>
          </div>
          <div class="flex justify-between py-1 border-b border-gray-800">
            <span class="text-gray-400">Test Beds Tested:</span>
            <span class="font-bold text-emerald-400">3,050 Tested</span>
          </div>
          <div class="flex justify-between py-1 border-b border-gray-800">
            <span class="text-gray-400">Breakdown Incidents:</span>
            <span class="font-bold text-white">20</span>
          </div>
          <div class="flex justify-between py-1 border-b border-gray-800">
            <span class="text-gray-400">Production Loss:</span>
            <span class="font-bold text-blue-400">16.5 Engines</span>
          </div>
          <div class="flex justify-between py-1">
            <span class="text-gray-400">Downtime:</span>
            <span class="font-bold text-amber-300">4.2 Hours</span>
          </div>
        </div>
      </div>

      <!-- Shift II -->
      <div class="glass-card rounded-xl p-5 border-t-4 border-rose-500">
        <div class="flex items-center justify-between">
          <h4 class="text-base font-bold text-white">Shift II (Peak Daytime)</h4>
          <span class="badge-critical text-xs px-2 py-0.5 rounded font-mono font-bold">56.7% Loss</span>
        </div>
        <p class="text-xs text-gray-400 mt-1">Highest load, line bottlenecks & peak heat</p>
        <div class="mt-4 space-y-2 text-xs">
          <div class="flex justify-between py-1 border-b border-gray-800">
            <span class="text-gray-400">Assembly Manned vs Actual:</span>
            <span class="font-bold text-white">19,606 / 27,308 (71.8%)</span>
          </div>
          <div class="flex justify-between py-1 border-b border-gray-800">
            <span class="text-gray-400">Test Beds Tested:</span>
            <span class="font-bold text-emerald-400">19,819 Tested</span>
          </div>
          <div class="flex justify-between py-1 border-b border-gray-800">
            <span class="text-gray-400">Breakdown Incidents:</span>
            <span class="font-bold text-rose-400 font-bold">431 Incidents</span>
          </div>
          <div class="flex justify-between py-1 border-b border-gray-800">
            <span class="text-gray-400">Production Loss:</span>
            <span class="font-bold text-rose-400 font-bold">572.0 Engines</span>
          </div>
          <div class="flex justify-between py-1">
            <span class="text-gray-400">Downtime:</span>
            <span class="font-bold text-rose-300 font-bold">132.1 Hours (62.3%)</span>
          </div>
        </div>
      </div>

      <!-- Shift III -->
      <div class="glass-card rounded-xl p-5 border-t-4 border-amber-500">
        <div class="flex items-center justify-between">
          <h4 class="text-base font-bold text-white">Shift III (Night Shift)</h4>
          <span class="badge-vital text-xs px-2 py-0.5 rounded font-mono font-bold">41.6% Loss</span>
        </div>
        <p class="text-xs text-gray-400 mt-1">High volume testing & conveyor indexing</p>
        <div class="mt-4 space-y-2 text-xs">
          <div class="flex justify-between py-1 border-b border-gray-800">
            <span class="text-gray-400">Assembly Manned vs Actual:</span>
            <span class="font-bold text-white">18,648 / 24,727 (75.4%)</span>
          </div>
          <div class="flex justify-between py-1 border-b border-gray-800">
            <span class="text-gray-400">Test Beds Tested:</span>
            <span class="font-bold text-emerald-400">20,960 Tested</span>
          </div>
          <div class="flex justify-between py-1 border-b border-gray-800">
            <span class="text-gray-400">Breakdown Incidents:</span>
            <span class="font-bold text-amber-400 font-bold">280 Incidents</span>
          </div>
          <div class="flex justify-between py-1 border-b border-gray-800">
            <span class="text-gray-400">Production Loss:</span>
            <span class="font-bold text-amber-400 font-bold">419.5 Engines</span>
          </div>
          <div class="flex justify-between py-1">
            <span class="text-gray-400">Downtime:</span>
            <span class="font-bold text-amber-300 font-bold">75.7 Hours (35.7%)</span>
          </div>
        </div>
      </div>

    </div>

    <!-- Monthly Evolution Table -->
    <div class="glass-card rounded-xl p-5">
      <h3 class="text-base font-bold text-white mb-3">Monthly Production & Maintenance Breakdown (FY 2026-27)</h3>
      <div class="overflow-x-auto">
        <table class="w-full text-left text-xs font-mono">
          <thead class="text-[11px] uppercase tracking-wider bg-gray-900/90 text-gray-400 border-b border-gray-800 font-sans">
            <tr>
              <th class="p-3 font-semibold">Month</th>
              <th class="p-3 font-semibold text-right">Shop 2 EA</th>
              <th class="p-3 font-semibold text-right">Shop 5 EA</th>
              <th class="p-3 font-semibold text-right text-emerald-400">Total Assembly</th>
              <th class="p-3 font-semibold text-right">Shop 2 TB</th>
              <th class="p-3 font-semibold text-right">Shop 5 TB</th>
              <th class="p-3 font-semibold text-right text-emerald-400">Total Passed TB</th>
              <th class="p-3 font-semibold text-right">Incidents</th>
              <th class="p-3 font-semibold text-right text-rose-400">Losses (Nos)</th>
              <th class="p-3 font-semibold text-right text-amber-300">Downtime (Hrs)</th>
            </tr>
          </thead>
          <tbody id="monthlyTableBody" class="divide-y divide-gray-800/60">
          </tbody>
        </table>
      </div>
    </div>

  </div>

  <!-- ================= TAB 6: INCIDENT LOG EXPLORER ================= -->
  <div id="tabContent-explorer" class="tab-pane hidden space-y-6">
    <div class="glass-card rounded-xl p-5">
      <div class="flex flex-col md:flex-row md:items-center md:justify-between gap-4 mb-4">
        <div>
          <h3 class="text-lg font-bold text-white">Complete Breakdown Incident Explorer</h3>
          <p class="text-xs text-gray-400">Searchable repository of all 731 breakdown maintenance interventions with actions & root causes</p>
        </div>
        <div class="flex flex-wrap items-center gap-3">
          <input type="text" id="incidentSearchInput" onkeyup="filterIncidents()" placeholder="Filter by text, failure, asset, action..." class="bg-gray-900 border border-gray-700 text-xs text-white px-3 py-1.5 rounded-lg focus:outline-none focus:border-blue-500 w-72">
          <select id="incidentShopFilter" onchange="filterIncidents()" class="bg-gray-900 border border-gray-700 text-xs text-white px-3 py-1.5 rounded-lg focus:outline-none focus:border-blue-500">
            <option value="ALL">All Shops</option>
            <option value="Shop 2">Shop 2</option>
            <option value="Shop 5">Shop 5</option>
          </select>
          <select id="incidentShiftFilter" onchange="filterIncidents()" class="bg-gray-900 border border-gray-700 text-xs text-white px-3 py-1.5 rounded-lg focus:outline-none focus:border-blue-500">
            <option value="ALL">All Shifts</option>
            <option value="I">Shift I</option>
            <option value="II">Shift II</option>
            <option value="III">Shift III</option>
          </select>
        </div>
      </div>

      <div class="text-xs text-gray-400 mb-2 flex items-center justify-between">
        <span id="incidentCountLabel">Showing 731 incidents</span>
        <span>Page <span id="currentPageNum">1</span> of <span id="totalPageNum">25</span></span>
      </div>

      <div class="overflow-x-auto">
        <table class="w-full text-left text-xs">
          <thead class="text-[11px] uppercase tracking-wider bg-gray-900/90 text-gray-400 border-b border-gray-800 font-sans">
            <tr>
              <th class="p-2.5 font-semibold">Date</th>
              <th class="p-2.5 font-semibold">Shop/Line</th>
              <th class="p-2.5 font-semibold">Shift</th>
              <th class="p-2.5 font-semibold">Asset ID</th>
              <th class="p-2.5 font-semibold">Machine Make</th>
              <th class="p-2.5 font-semibold text-rose-400 text-right">Loss</th>
              <th class="p-2.5 font-semibold text-amber-300 text-right">Downtime</th>
              <th class="p-2.5 font-semibold">Abnormality & Problem Description</th>
              <th class="p-2.5 font-semibold">Root Cause & Mechanism</th>
              <th class="p-2.5 font-semibold">Immediate Action Taken</th>
              <th class="p-2.5 font-semibold text-center">Status</th>
            </tr>
          </thead>
          <tbody id="incidentTableBody" class="divide-y divide-gray-800/60 font-sans text-xs">
          </tbody>
        </table>
      </div>

      <!-- Pagination -->
      <div class="flex items-center justify-between pt-4 mt-2 border-t border-gray-800">
        <button onclick="prevIncidentPage()" class="px-3 py-1.5 bg-gray-800 hover:bg-gray-700 text-xs text-gray-300 rounded border border-gray-700">Previous</button>
        <div class="flex gap-1" id="paginationControls"></div>
        <button onclick="nextIncidentPage()" class="px-3 py-1.5 bg-gray-800 hover:bg-gray-700 text-xs text-gray-300 rounded border border-gray-700">Next</button>
      </div>
    </div>
  </div>

  <!-- ================= TAB 7: ENGINEERING ACTION MATRIX ================= -->
  <div id="tabContent-actions" class="tab-pane hidden space-y-6">
    <div class="glass-card rounded-xl p-6">
      <h3 class="text-lg font-bold text-white mb-2">Strategic Maintenance & Reliability Engineering Action Matrix</h3>
      <p class="text-xs text-gray-400 mb-6">Targeted counter-measures formulated from 6.5-month empirical breakdown logs and root-cause clustering</p>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        
        <!-- Priority 1: Long Block Conveyor -->
        <div class="p-4 rounded-xl bg-gray-900/80 border border-red-500/30">
          <div class="flex items-center gap-2 mb-2">
            <span class="badge-critical text-xs px-2 py-0.5 rounded font-bold">PRIORITY 1 - HIGH FREQUENCY</span>
            <span class="text-xs text-gray-400 font-mono">LM03925 / L2EA</span>
          </div>
          <h4 class="text-sm font-bold text-white">Long Block Conveyor RFID & Workover Desynchronization</h4>
          <p class="text-xs text-gray-300 mt-1.5 leading-relaxed">
            <strong>Finding:</strong> 74 breakdowns resulting in 83 lost engines. 80%+ were resolved by manual "Bit reset done" or "Manual read/write".
          </p>
          <div class="mt-3 p-3 bg-gray-800/60 rounded-lg text-xs space-y-1.5 text-gray-300">
            <div class="text-emerald-400 font-semibold">Recommended Corrective Actions:</div>
            <div>• Replace aging RFID read heads at Station 01, 09, 18, 19 with high-noise-immunity industrial readers.</div>
            <div>• Implement automatic software retry logic in PLC rather than latching into hard workover timeout.</div>
            <div>• Reinforce mechanical stoppers & photo-eye alignments at Station 19 buffer shunting trolley to prevent pallet mis-seating.</div>
          </div>
        </div>

        <!-- Priority 2: TB505 Diesel Test Cell -->
        <div class="p-4 rounded-xl bg-gray-900/80 border border-red-500/30">
          <div class="flex items-center gap-2 mb-2">
            <span class="badge-critical text-xs px-2 py-0.5 rounded font-bold">PRIORITY 2 - HIGH DOWNTIME</span>
            <span class="text-xs text-gray-400 font-mono">LA10025 / L1TB</span>
          </div>
          <h4 class="text-sm font-bold text-white">TB505 Chronic Downtime (2,116 Mins / 35.3 Hours)</h4>
          <p class="text-xs text-gray-300 mt-1.5 leading-relaxed">
            <strong>Finding:</strong> 55 breakdown events with multiple lengthy DDC Q-station failures, fuel airlocks, and cooling tower water pressure drops.
          </p>
          <div class="mt-3 p-3 bg-gray-800/60 rounded-lg text-xs space-y-1.5 text-gray-300">
            <div class="text-emerald-400 font-semibold">Recommended Corrective Actions:</div>
            <div>• Install an automated air-bleed / priming valve on TB505 fuel delivery manifold to eliminate manual priming delays.</div>
            <div>• Overhaul cooling tower sump buffer water feed pumps with automatic level sensor interlocks.</div>
            <div>• Dedicated isolated 24V DC power supply for Gantner and DDC communications to prevent intermittent network dropouts.</div>
          </div>
        </div>

        <!-- Priority 3: DC Fastening Nutrunners -->
        <div class="p-4 rounded-xl bg-gray-900/80 border border-amber-500/30">
          <div class="flex items-center gap-2 mb-2">
            <span class="badge-vital text-xs px-2 py-0.5 rounded font-bold">PRIORITY 3 - ASSEMBLY CRITICAL</span>
            <span class="text-xs text-gray-400 font-mono">LA11693, LA11901, HS5DC003</span>
          </div>
          <h4 class="text-sm font-bold text-white">Multi-Spindle & DC Nutrunner Encoder Jumping & Socket Catchup</h4>
          <p class="text-xs text-gray-300 mt-1.5 leading-relaxed">
            <strong>Finding:</strong> 140 incidents across DC tools and head nutrunners (202 engine losses). Recurrent encoder jumping on Estic tools and Rexroth LT350 module failure.
          </p>
          <div class="mt-3 p-3 bg-gray-800/60 rounded-lg text-xs space-y-1.5 text-gray-300">
            <div class="text-emerald-400 font-semibold">Recommended Corrective Actions:</div>
            <div>• Weekly PM schedule for spring balancers, socket spring tensioners, and locating dowels on HCH and 26-Spindle runners.</div>
            <div>• Standardize DOGA arm vertical encoder cable strain relief brackets to avoid intermittent pin disconnects.</div>
            <div>• Keep pre-parameterized spare drive modules (Rexroth LT350 / Bosch VM300) in hot standby on the line.</div>
          </div>
        </div>

        <!-- Priority 4: CNG & Quality Inspection -->
        <div class="p-4 rounded-xl bg-gray-900/80 border border-blue-500/30">
          <div class="flex items-center gap-2 mb-2">
            <span class="badge-blue text-xs px-2 py-0.5 rounded font-bold">PRIORITY 4 - QUALITY ASSURANCE</span>
            <span class="text-xs text-gray-400 font-mono">PA640001 (P15), LA11985 (IPV-2)</span>
          </div>
          <h4 class="text-sm font-bold text-white">P15 CNG Rejection Rate & Vision Inspection PC Storage</h4>
          <p class="text-xs text-gray-300 mt-1.5 leading-relaxed">
            <strong>Finding:</strong> P15 CNG test bed exhibits a 15% first-time rejection rate (239 retests), while IPV-2 Piston verification suffered a 75-min breakdown due to PC disk storage exhaustion.
          </p>
          <div class="mt-3 p-3 bg-gray-800/60 rounded-lg text-xs space-y-1.5 text-gray-300">
            <div class="text-emerald-400 font-semibold">Recommended Corrective Actions:</div>
            <div>• Perform full calibration and sensor loop validation on P15 CNG dyno to eliminate false-positive aborts.</div>
            <div>• Deploy automated daily disk cleanup & image archival scripts on all SigPod and Cognex vision PCs.</div>
            <div>• Protect 3-pin Denso trigger wheel sensor harness on IPV-2 station with heavy-duty spiral armor wrap.</div>
          </div>
        </div>

      </div>
    </div>
  </div>

  <!-- MODAL FOR INCIDENT / MACHINE DETAILS -->
  <div id="detailModal" class="fixed inset-0 bg-black/80 backdrop-blur-sm z-50 flex items-center justify-center hidden p-4">
    <div class="bg-gray-900 border border-gray-700 rounded-2xl max-w-2xl w-full p-6 relative text-xs text-gray-300 shadow-2xl">
      <button onclick="closeModal()" class="absolute top-4 right-4 text-gray-400 hover:text-white text-lg font-bold">✕</button>
      <div id="modalContent"></div>
    </div>
  </div>

  <!-- EMBEDDED DATA SCRIPT -->
  <script>
    const KPI_DATA = {json_str};

    // Initialize Dashboard
    document.addEventListener("DOMContentLoaded", function() {{
      renderMonthlyChart();
      renderShiftDonut();
      renderTop5List();
      renderMachineTable();
      renderTestCellTable();
      renderSubsystemList();
      renderAbnormalityList();
      renderMonthlyTable();
      renderIncidentTable();
    }});

    function switchTab(tabId) {{
      document.querySelectorAll(".tab-pane").forEach(el => el.classList.add("hidden"));
      document.querySelectorAll(".nav-tab").forEach(el => el.classList.remove("active"));
      
      const pane = document.getElementById("tabContent-" + tabId);
      if (pane) pane.classList.remove("hidden");
      
      const btn = document.getElementById("tabBtn-" + tabId);
      if (btn) btn.classList.add("active");
    }}

    // 1. Monthly SVG Chart
    function renderMonthlyChart() {{
      const container = document.getElementById("monthlyChartContainer");
      const trends = KPI_DATA.monthly_trends;
      
      const maxVal = Math.max(...trends.map(t => Math.max(t.s2_ea_manned + t.s5_ea_manned, t.ea_total_actual))) * 1.15;
      const width = 640;
      const height = 220;
      const padding = {{ top: 20, right: 20, bottom: 35, left: 50 }};
      const chartW = width - padding.left - padding.right;
      const chartH = height - padding.top - padding.bottom;
      
      const barWidth = 24;
      const step = chartW / trends.length;
      
      let svg = `<svg viewBox="0 0 ${{width}} ${{height}}" class="w-full h-full">`;
      
      // Grid lines
      for (let i = 0; i <= 4; i++) {{
        const y = padding.top + (chartH / 4) * i;
        const val = Math.round(maxVal - (maxVal / 4) * i);
        svg += `<line x1="${{padding.left}}" y1="${{y}}" x2="${{width - padding.right}}" y2="${{y}}" stroke="#1f2937" stroke-dasharray="3,3"/>`;
        svg += `<text x="${{padding.left - 8}}" y="${{y + 4}}" fill="#6b7280" font-size="10" text-anchor="end" font-family="monospace">${{val.toLocaleString()}}</text>`;
      }}
      
      // Bars and Points
      trends.forEach((t, i) => {{
        const xCenter = padding.left + i * step + step / 2;
        const manned = t.s2_ea_manned + t.s5_ea_manned;
        const actual = t.ea_total_actual;
        
        const hManned = (manned / maxVal) * chartH;
        const hActual = (actual / maxVal) * chartH;
        
        const yManned = padding.top + chartH - hManned;
        const yActual = padding.top + chartH - hActual;
        
        // Manned bar (blue)
        svg += `<rect x="${{xCenter - barWidth - 2}}" y="${{yManned}}" width="${{barWidth}}" height="${{hManned}}" fill="#3b82f6" rx="3" opacity="0.85">
          <title>${{t.label}} Plan Manned: ${{manned.toLocaleString()}}</title>
        </rect>`;
        
        // Actual bar (emerald)
        svg += `<rect x="${{xCenter + 2}}" y="${{yActual}}" width="${{barWidth}}" height="${{hActual}}" fill="#10b981" rx="3">
          <title>${{t.label}} Output Passed: ${{actual.toLocaleString()}} (${{Math.round(actual/manned*100)}}%)</title>
        </rect>`;
        
        // Value on top of actual bar
        svg += `<text x="${{xCenter + 2 + barWidth/2}}" y="${{yActual - 5}}" fill="#34d399" font-size="9" text-anchor="middle" font-weight="bold">${{actual.toLocaleString()}}</text>`;
        
        // X-axis label
        svg += `<text x="${{xCenter}}" y="${{height - 10}}" fill="#9ca3af" font-size="11" text-anchor="middle" font-weight="500">${{t.label}}</text>`;
      }});
      
      svg += `</svg>`;
      container.innerHTML = svg;
    }}

    // 2. Shift Donut Chart
    function renderShiftDonut() {{
      const container = document.getElementById("shiftDonutContainer");
      const shifts = KPI_DATA.shift_performance;
      const totalLoss = shifts.reduce((acc, s) => acc + s.bd_loss_nos, 0);
      
      const cx = 85, cy = 85, r = 65, strokeW = 24;
      const circum = 2 * Math.PI * r;
      
      const colors = ["#3b82f6", "#f43f5e", "#f59e0b"]; // Shift I, II, III
      let offset = 0;
      
      let svg = `<svg viewBox="0 0 170 170" class="w-36 h-36">`;
      shifts.forEach((s, i) => {{
        const pct = s.bd_loss_nos / totalLoss;
        const dash = pct * circum;
        svg += `<circle cx="${{cx}}" cy="${{cy}}" r="${{r}}" fill="transparent" stroke="${{colors[i]}}" stroke-width="${{strokeW}}"
                  stroke-dasharray="${{dash}} ${{circum}}" stroke-dashoffset="${{-offset}}" transform="rotate(-90 ${{cx}} ${{cy}})">
                  <title>${{s.shift}}: ${{s.bd_loss_nos}} Losses (${{(pct*100).toFixed(1)}}%)</title>
                </circle>`;
        offset += dash;
      }});
      
      svg += `<text x="${{cx}}" y="${{cy - 4}}" fill="#ffffff" font-size="16" font-weight="bold" text-anchor="middle" font-family="monospace">1,008</text>`;
      svg += `<text x="${{cx}}" y="${{cy + 14}}" fill="#9ca3af" font-size="9" text-anchor="middle">TOTAL LOSS</text>`;
      svg += `</svg>`;
      
      container.innerHTML = svg;
    }}

    // 3. Render Top 5 Loss Machines List
    function renderTop5List() {{
      const list = document.getElementById("top5LossList");
      const top5 = KPI_DATA.top_loss_machines.slice(0, 5);
      
      let html = "";
      top5.forEach((m, idx) => {{
        const lossPct = Math.round((m.total_loss_nos / 1008) * 100);
        html += `
          <div class="p-3 rounded-lg bg-gray-800/40 border border-gray-700/50 hover:bg-gray-800/70 transition flex items-center justify-between cursor-pointer" onclick="showMachineDetail('${{m.asset_id}}')">
            <div class="flex items-center gap-3">
              <span class="w-6 h-6 rounded-full flex items-center justify-center font-bold text-xs bg-gray-700 text-white">${{idx + 1}}</span>
              <div>
                <div class="font-bold text-white flex items-center gap-2">
                  <span>${{m.make}}</span>
                  <span class="text-[11px] text-gray-400 font-mono">(${{m.asset_id}})</span>
                </div>
                <div class="text-[11px] text-gray-400 mt-0.5">
                  <span class="text-blue-400 font-semibold">${{m.line}}</span> • ${{m.shop}} • ${{m.bd_count}} incidents • MTTR: ${{m.mttr_mins}}m
                </div>
              </div>
            </div>
            <div class="text-right">
              <div class="text-sm font-bold text-rose-400">${{m.total_loss_nos}} Loss</div>
              <div class="text-[11px] text-amber-300 font-mono">${{m.total_downtime_hrs}}h downtime</div>
            </div>
          </div>
        `;
      }});
      list.innerHTML = html;
    }}

    // 4. Render Machine Table
    function renderMachineTable() {{
      const tbody = document.getElementById("machineTableBody");
      const machines = KPI_DATA.top_loss_machines;
      
      let html = "";
      machines.forEach((m, idx) => {{
        html += `
          <tr class="hover:bg-gray-800/50 transition">
            <td class="p-3 text-gray-400">${{idx + 1}}</td>
            <td class="p-3 font-bold text-blue-400">${{m.asset_id}}</td>
            <td class="p-3 font-sans font-medium text-white">${{m.make}}</td>
            <td class="p-3 text-gray-300">${{m.line}} (${{m.shop}})</td>
            <td class="p-3 text-center"><span class="badge-vital px-2 py-0.5 rounded text-[10px] font-bold">${{m.criticality}}</span></td>
            <td class="p-3 text-right text-white">${{m.bd_count}}</td>
            <td class="p-3 text-right font-bold text-rose-400">${{m.total_loss_nos}}</td>
            <td class="p-3 text-right text-amber-300 font-bold">${{m.total_downtime_hrs}} hrs</td>
            <td class="p-3 text-right text-cyan-300">${{m.mttr_mins}}</td>
            <td class="p-3 text-center">
              <button onclick="showMachineDetail('${{m.asset_id}}')" class="px-2 py-1 rounded bg-blue-900/60 hover:bg-blue-800 text-blue-300 text-[11px] font-sans">
                Analyze
              </button>
            </td>
          </tr>
        `;
      }});
      tbody.innerHTML = html;
    }}

    function filterMachineTable() {{
      const q = document.getElementById("machineSearchInput").value.toLowerCase();
      const rows = document.querySelectorAll("#machineTableBody tr");
      rows.forEach(r => {{
        const text = r.innerText.toLowerCase();
        r.style.display = text.includes(q) ? "" : "none";
      }});
    }}

    // 5. Render Test Cells
    function renderTestCellTable() {{
      const tbody = document.getElementById("testCellTableBody");
      const cells = KPI_DATA.test_cells;
      
      let html = "";
      cells.forEach(c => {{
        const passColor = c.pass_rate >= 97 ? "text-emerald-400 font-bold" : (c.pass_rate >= 94 ? "text-amber-400 font-bold" : "text-rose-400 font-bold");
        html += `
          <tr class="hover:bg-gray-800/50 transition">
            <td class="p-2.5 font-bold text-blue-400">${{c.asset_id}}</td>
            <td class="p-2.5 font-sans font-medium text-white">${{c.make}}</td>
            <td class="p-2.5 text-gray-300">${{c.line}}</td>
            <td class="p-2.5 text-right font-bold text-white">${{c.tested.toLocaleString()}}</td>
            <td class="p-2.5 text-right text-emerald-400">${{c.passed.toLocaleString()}}</td>
            <td class="p-2.5 text-right text-gray-400">${{c.rejections.toLocaleString()}}</td>
            <td class="p-2.5 text-right ${{passColor}}">${{c.pass_rate}}%</td>
            <td class="p-2.5 text-right text-rose-400 font-bold">${{c.bd_loss_nos}}</td>
            <td class="p-2.5 text-right text-amber-300">${{c.bd_downtime_hrs}}</td>
          </tr>
        `;
      }});
      tbody.innerHTML = html;
    }}

    // 6. Subsystem Pareto
    function renderSubsystemList() {{
      const list = document.getElementById("subsystemList");
      const subs = KPI_DATA.subsystem_pareto;
      const maxLoss = subs[0].loss_nos;
      
      let html = "";
      subs.forEach((s, idx) => {{
        const pct = Math.round((s.loss_nos / maxLoss) * 100);
        html += `
          <div class="p-3 rounded-lg bg-gray-800/40 border border-gray-700/50">
            <div class="flex items-center justify-between text-xs mb-1.5">
              <span class="font-bold text-white">${{idx + 1}}. ${{s.category}}</span>
              <span class="font-mono text-rose-400 font-bold">${{s.loss_nos}} Losses <span class="text-gray-400">(${{s.incidents}} inc, ${{s.downtime_hrs}}h)</span></span>
            </div>
            <div class="w-full bg-gray-900 h-2 rounded-full overflow-hidden">
              <div class="bg-gradient-to-r from-blue-500 to-rose-500 h-full rounded-full" style="width: ${{pct}}%"></div>
            </div>
          </div>
        `;
      }});
      list.innerHTML = html;
    }}

    // 7. Abnormality Pareto
    function renderAbnormalityList() {{
      const list = document.getElementById("abnormalityList");
      const abs = KPI_DATA.common_abnormalities.slice(0, 10);
      
      let html = "";
      abs.forEach((a, idx) => {{
        html += `
          <div class="p-3 rounded-lg bg-gray-800/40 border border-gray-700/50">
            <div class="flex items-start justify-between gap-2">
              <div>
                <div class="font-semibold text-white">${{idx + 1}}. ${{a.abnormality}}</div>
                <div class="text-[11px] text-gray-400 mt-0.5">Root cause: ${{a.root_cause || "Hardware / sensor glitch"}}</div>
              </div>
              <div class="text-right whitespace-nowrap">
                <span class="badge-critical text-[10px] px-2 py-0.5 rounded font-bold">${{a.total_loss}} Loss</span>
                <div class="text-[10px] text-gray-400 mt-0.5">${{a.count}} Occurrences</div>
              </div>
            </div>
          </div>
        `;
      }});
      list.innerHTML = html;
    }}

    // 8. Monthly Table
    function renderMonthlyTable() {{
      const tbody = document.getElementById("monthlyTableBody");
      const trends = KPI_DATA.monthly_trends;
      
      let html = "";
      trends.forEach(t => {{
        html += `
          <tr class="hover:bg-gray-800/50 transition">
            <td class="p-3 font-sans font-bold text-white">${{t.label}}</td>
            <td class="p-3 text-right text-gray-300">${{t.s2_ea_actual.toLocaleString()}} <span class="text-gray-500 text-[10px]">/ ${{t.s2_ea_manned.toLocaleString()}}</span></td>
            <td class="p-3 text-right text-gray-300">${{t.s5_ea_actual.toLocaleString()}} <span class="text-gray-500 text-[10px]">/ ${{t.s5_ea_manned.toLocaleString()}}</span></td>
            <td class="p-3 text-right font-bold text-emerald-400">${{t.ea_total_actual.toLocaleString()}}</td>
            <td class="p-3 text-right text-gray-300">${{t.s2_tb_passed.toLocaleString()}}</td>
            <td class="p-3 text-right text-gray-300">${{t.s5_tb_passed.toLocaleString()}}</td>
            <td class="p-3 text-right font-bold text-emerald-400">${{t.tb_total_passed.toLocaleString()}}</td>
            <td class="p-3 text-right text-white">${{t.bd_incidents}}</td>
            <td class="p-3 text-right font-bold text-rose-400">${{t.bd_losses}}</td>
            <td class="p-3 text-right text-amber-300 font-bold">${{(t.bd_downtime_mins/60).toFixed(1)}}</td>
          </tr>
        `;
      }});
      tbody.innerHTML = html;
    }}

    // 9. Incident Log Explorer with Pagination
    let currentIncidentPage = 1;
    const incidentsPerPage = 25;
    let filteredIncidents = KPI_DATA.all_breakdowns || [];

    function renderIncidentTable() {{
      const tbody = document.getElementById("incidentTableBody");
      const start = (currentIncidentPage - 1) * incidentsPerPage;
      const end = start + incidentsPerPage;
      const pageData = filteredIncidents.slice(start, end);
      
      document.getElementById("incidentCountLabel").innerText = `Showing ${{filteredIncidents.length}} incidents (Page ${{currentIncidentPage}} of ${{Math.ceil(filteredIncidents.length / incidentsPerPage) || 1}})`;
      document.getElementById("currentPageNum").innerText = currentIncidentPage;
      document.getElementById("totalPageNum").innerText = Math.ceil(filteredIncidents.length / incidentsPerPage) || 1;

      let html = "";
      pageData.forEach(inc => {{
        const statusBadge = inc.status === "OK" ? "badge-success" : (inc.status.includes("OBSERVATION") ? "badge-vital" : "badge-critical");
        html += `
          <tr class="hover:bg-gray-800/50 transition">
            <td class="p-2.5 font-mono text-[11px] text-gray-400 whitespace-nowrap">${{inc.date}}</td>
            <td class="p-2.5 font-medium text-blue-400 whitespace-nowrap">${{inc.shop}} (${{inc.line}})</td>
            <td class="p-2.5 font-bold text-gray-300">${{inc.shift}}</td>
            <td class="p-2.5 font-mono font-bold text-white">${{inc.asset_id}}</td>
            <td class="p-2.5 font-medium text-gray-200">${{inc.make}}</td>
            <td class="p-2.5 text-right font-mono font-bold text-rose-400">${{inc.loss_nos}}</td>
            <td class="p-2.5 text-right font-mono text-amber-300">${{inc.downtime_mins}}m</td>
            <td class="p-2.5 text-gray-300 max-w-xs truncate" title="${{inc.abnormality}}">${{inc.abnormality || "Operational disruption"}}</td>
            <td class="p-2.5 text-gray-400 max-w-xs truncate" title="${{inc.root_cause}}">${{inc.root_cause || "—"}}</td>
            <td class="p-2.5 text-gray-300 max-w-xs truncate" title="${{inc.action_taken}}">${{inc.action_taken || "Restored"}}</td>
            <td class="p-2.5 text-center"><span class="${{statusBadge}} text-[10px] px-2 py-0.5 rounded font-bold">${{inc.status}}</span></td>
          </tr>
        `;
      }});
      tbody.innerHTML = html;
      renderPaginationControls();
    }}

    function filterIncidents() {{
      const q = document.getElementById("incidentSearchInput").value.toLowerCase();
      const shop = document.getElementById("incidentShopFilter").value;
      const shift = document.getElementById("incidentShiftFilter").value;
      
      filteredIncidents = KPI_DATA.all_breakdowns.filter(inc => {{
        const matchShop = (shop === "ALL") || (inc.shop === shop);
        const matchShift = (shift === "ALL") || (inc.shift === shift);
        const matchText = !q || (
          (inc.asset_id && inc.asset_id.toLowerCase().includes(q)) ||
          (inc.make && inc.make.toLowerCase().includes(q)) ||
          (inc.abnormality && inc.abnormality.toLowerCase().includes(q)) ||
          (inc.root_cause && inc.root_cause.toLowerCase().includes(q)) ||
          (inc.action_taken && inc.action_taken.toLowerCase().includes(q)) ||
          (inc.date && inc.date.includes(q))
        );
        return matchShop && matchShift && matchText;
      }});
      
      currentIncidentPage = 1;
      renderIncidentTable();
    }}

    function prevIncidentPage() {{
      if (currentIncidentPage > 1) {{
        currentIncidentPage--;
        renderIncidentTable();
      }}
    }}

    function nextIncidentPage() {{
      const maxPages = Math.ceil(filteredIncidents.length / incidentsPerPage);
      if (currentIncidentPage < maxPages) {{
        currentIncidentPage++;
        renderIncidentTable();
      }}
    }}

    function renderPaginationControls() {{
      const maxPages = Math.ceil(filteredIncidents.length / incidentsPerPage) || 1;
      const container = document.getElementById("paginationControls");
      let html = "";
      
      let startP = Math.max(1, currentIncidentPage - 2);
      let endP = Math.min(maxPages, startP + 4);
      if (endP - startP < 4) startP = Math.max(1, endP - 4);
      
      for (let p = startP; p <= endP; p++) {{
        const active = p === currentIncidentPage ? "bg-blue-600 text-white font-bold" : "bg-gray-800 text-gray-400 hover:bg-gray-700";
        html += `<button onclick="goToIncidentPage(${{p}})" class="px-2.5 py-1 text-xs rounded border border-gray-700 ${{active}}">${{p}}</button>`;
      }}
      container.innerHTML = html;
    }}

    function goToIncidentPage(p) {{
      currentIncidentPage = p;
      renderIncidentTable();
    }}

    // Modal Details
    function showMachineDetail(assetId) {{
      const m = KPI_DATA.top_loss_machines.find(x => x.asset_id === assetId) || KPI_DATA.test_cells.find(x => x.asset_id === assetId);
      if (!m) return;
      
      const relatedBds = KPI_DATA.all_breakdowns.filter(b => b.asset_id === assetId);
      
      let modalHtml = `
        <div class="border-b border-gray-800 pb-3 mb-4">
          <div class="flex items-center justify-between">
            <span class="badge-blue text-xs px-2.5 py-1 rounded font-bold">${{m.asset_id}}</span>
            <span class="badge-critical text-xs px-2.5 py-1 rounded font-bold">${{m.criticality || "VITAL"}} ASSET</span>
          </div>
          <h2 class="text-xl font-black text-white mt-2">${{m.make}}</h2>
          <div class="text-xs text-gray-400 mt-1">${{m.shop}} • Line: ${{m.line}}</div>
        </div>

        <div class="grid grid-cols-4 gap-3 text-center mb-5">
          <div class="p-2.5 bg-gray-800/60 rounded-lg">
            <div class="text-gray-400 text-[10px] uppercase font-semibold">Breakdowns</div>
            <div class="text-lg font-bold text-white font-mono mt-0.5">${{m.bd_count}}</div>
          </div>
          <div class="p-2.5 bg-gray-800/60 rounded-lg">
            <div class="text-gray-400 text-[10px] uppercase font-semibold">Engines Lost</div>
            <div class="text-lg font-bold text-rose-400 font-mono mt-0.5">${{m.total_loss_nos || m.bd_loss_nos}}</div>
          </div>
          <div class="p-2.5 bg-gray-800/60 rounded-lg">
            <div class="text-gray-400 text-[10px] uppercase font-semibold">Downtime</div>
            <div class="text-lg font-bold text-amber-300 font-mono mt-0.5">${{m.total_downtime_hrs || m.bd_downtime_hrs}}h</div>
          </div>
          <div class="p-2.5 bg-gray-800/60 rounded-lg">
            <div class="text-gray-400 text-[10px] uppercase font-semibold">MTTR</div>
            <div class="text-lg font-bold text-cyan-300 font-mono mt-0.5">${{m.mttr_mins || ((m.bd_downtime_mins/m.bd_count)||0).toFixed(1)}}m</div>
          </div>
        </div>

        <h4 class="font-bold text-white text-xs mb-2">Historical Incident Highlights (${{relatedBds.length}} Total):</h4>
        <div class="space-y-2 max-h-56 overflow-y-auto pr-1 custom-scrollbar">
      `;

      if (relatedBds.length === 0) {{
        modalHtml += `<div class="text-gray-500 text-center py-4">No breakdown incidents recorded for this asset.</div>`;
      }} else {{
        relatedBds.slice(0, 10).forEach(b => {{
          modalHtml += `
            <div class="p-2.5 bg-gray-800/40 rounded border border-gray-800 text-xs">
              <div class="flex justify-between items-center text-[11px] text-gray-400 font-mono mb-1">
                <span>${{b.date}} • ${{b.shift}}</span>
                <span class="text-rose-400 font-bold">${{b.loss_nos}} Loss • ${{b.downtime_mins}}m DT</span>
              </div>
              <div class="text-gray-200 font-medium">${{b.abnormality || "Issue logged"}}</div>
              <div class="text-gray-400 text-[11px] mt-0.5">Root: ${{b.root_cause || "Hardware/Network fault"}}</div>
              <div class="text-emerald-400 text-[11px] mt-0.5">Action: ${{b.action_taken || "Restored ok"}}</div>
            </div>
          `;
        }});
      }}

      modalHtml += `
        </div>
        <div class="mt-4 pt-3 border-t border-gray-800 text-right">
          <button onclick="closeModal()" class="px-4 py-1.5 bg-blue-600 hover:bg-blue-500 text-white rounded-lg text-xs font-semibold">Close</button>
        </div>
      `;

      document.getElementById("modalContent").innerHTML = modalHtml;
      document.getElementById("detailModal").classList.remove("hidden");
    }}

    function closeModal() {{
      document.getElementById("detailModal").classList.add("hidden");
    }}

    // Export CSV
    function exportBreakdownCSV() {{
      let csv = "ID,Date,Shop,Line,Shift,Asset_ID,Machine,Loss_Nos,Downtime_Mins,Abnormality,Root_Cause,Action_Taken,Status\\n";
      KPI_DATA.all_breakdowns.forEach(b => {{
        csv += `"${{b.id}}","${{b.date}}","${{b.shop}}","${{b.line}}","${{b.shift}}","${{b.asset_id}}","${{b.make}}",${{b.loss_nos}},${{b.downtime_mins}},"${{(b.abnormality||"").replace(/"/g, '""')}}","${{(b.root_cause||"").replace(/"/g, '""')}}","${{(b.action_taken||"").replace(/"/g, '""')}}","${{b.status}}"\\n`;
      }});
      
      const blob = new Blob([csv], {{ type: "text/csv;charset=utf-8;" }});
      const url = URL.createObjectURL(blob);
      const link = document.createElement("a");
      link.setAttribute("href", url);
      link.setAttribute("download", "HSeries_Breakdown_Maintenance_Log_FY2627.csv");
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }}

    // Global Shop Filter
    function applyGlobalFilter() {{
      const shop = document.getElementById("globalShopFilter").value;
      if (shop === "ALL") {{
        document.getElementById("kpiAssemblyActual").innerText = KPI_DATA.kpi_summary.total_ea_actual.toLocaleString();
        document.getElementById("kpiTestedTested").innerText = KPI_DATA.kpi_summary.total_tb_tested.toLocaleString();
        document.getElementById("kpiPassedCount").innerText = KPI_DATA.kpi_summary.total_tb_passed.toLocaleString() + " Passed";
        document.getElementById("kpiBDLoss").innerText = KPI_DATA.kpi_summary.total_bd_losses_nos.toLocaleString();
        document.getElementById("kpiDowntimeHours").innerText = KPI_DATA.kpi_summary.total_bd_downtime_hrs.toLocaleString();
      }} else if (shop === "Shop 2") {{
        document.getElementById("kpiAssemblyActual").innerText = KPI_DATA.kpi_summary.shop2_ea.actual.toLocaleString();
        document.getElementById("kpiTestedTested").innerText = KPI_DATA.kpi_summary.shop2_tb.tested.toLocaleString();
        document.getElementById("kpiPassedCount").innerText = KPI_DATA.kpi_summary.shop2_tb.passed.toLocaleString() + " Passed";
        document.getElementById("kpiBDLoss").innerText = (KPI_DATA.kpi_summary.shop2_ea.bd_loss_nos + KPI_DATA.kpi_summary.shop2_tb.bd_loss_nos).toLocaleString();
        document.getElementById("kpiDowntimeHours").innerText = (KPI_DATA.kpi_summary.shop2_ea.downtime_hrs + KPI_DATA.kpi_summary.shop2_tb.downtime_hrs).toFixed(1);
      }} else if (shop === "Shop 5") {{
        document.getElementById("kpiAssemblyActual").innerText = KPI_DATA.kpi_summary.shop5_ea.actual.toLocaleString();
        document.getElementById("kpiTestedTested").innerText = KPI_DATA.kpi_summary.shop5_tb.tested.toLocaleString();
        document.getElementById("kpiPassedCount").innerText = KPI_DATA.kpi_summary.shop5_tb.passed.toLocaleString() + " Passed";
        document.getElementById("kpiBDLoss").innerText = (KPI_DATA.kpi_summary.shop5_ea.bd_loss_nos + KPI_DATA.kpi_summary.shop5_tb.bd_loss_nos).toLocaleString();
        document.getElementById("kpiDowntimeHours").innerText = (KPI_DATA.kpi_summary.shop5_ea.downtime_hrs + KPI_DATA.kpi_summary.shop5_tb.downtime_hrs).toFixed(1);
      }}
    }}
  </script>

</body>
</html>'''

# Write to artifact dir and scratch dir
artifact_path = r'C:\Users\PS 4\.gemini\antigravity\brain\06588b09-1586-499f-b523-14929190a8f7\kpi_dashboard.html'
scratch_path = r'C:\Users\PS 4\.gemini\antigravity\scratch\kpi_dashboard\index.html'

with open(artifact_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

with open(scratch_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f'Successfully built dashboard HTML at {artifact_path} and {scratch_path}!')
