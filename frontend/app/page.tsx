"use client";

import { useState } from "react";
import { simplifyAssignment } from "../lib/api";

export default function Home() {
  const [text, setText] = useState("");
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  async function handleSimplify() {
    setLoading(true);
    setResult(null);

    try {
      const data = await simplifyAssignment(text);
      setResult(data.result);
    } catch (error) {
      alert("Something went wrong. Check your backend.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="min-h-screen p-8 bg-gray-50 text-gray-900">
      <section className="max-w-4xl mx-auto space-y-6">
        <h1 className="text-4xl font-bold">
          Instruction Simplifier
        </h1>

        <p className="text-lg">
          Paste academic instructions and turn them into a clear learning plan.
        </p>

        <textarea
          className="w-full h-64 p-4 border rounded-xl text-lg"
          placeholder="Paste assignment prompt, syllabus text, rubric, or instructor email..."
          value={text}
          onChange={(e) => setText(e.target.value)}
        />

        <button
          onClick={handleSimplify}
          className="px-6 py-3 rounded-xl bg-black text-white font-semibold"
        >
          {loading ? "Simplifying..." : "Simplify Instructions"}
        </button>

        {result && (
          <section className="space-y-4">
            <Card title="Plain Summary" content={result.plain_summary} />
            <Card title="Start Here" content={result.start_here} />
            <ListCard title="Checklist" items={result.checklist} />
            <ListCard title="Timeline" items={result.timeline} />
            <ListCard title="Deadlines" items={result.deadlines} />
            <ListCard title="Materials Needed" items={result.materials_needed} />
            <Card title="Rubric Simplified" content={result.rubric_simplified} />
            <Card title="Time Estimate" content={result.time_estimate} />
          </section>
        )}
      </section>
    </main>
  );
}

function Card({ title, content }: { title: string; content: string }) {
  return (
    <div className="p-5 bg-white rounded-xl shadow">
      <h2 className="text-xl font-bold mb-2">{title}</h2>
      <p>{content || "Not found"}</p>
    </div>
  );
}

function ListCard({ title, items }: { title: string; items: string[] }) {
  return (
    <div className="p-5 bg-white rounded-xl shadow">
      <h2 className="text-xl font-bold mb-2">{title}</h2>
      <ul className="list-disc pl-6 space-y-1">
        {items?.length ? (
          items.map((item, index) => <li key={index}>{item}</li>)
        ) : (
          <li>Not found</li>
        )}
      </ul>
    </div>
  );
}