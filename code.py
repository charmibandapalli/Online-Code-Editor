import React, { useState } from "react";
import { Controlled as CodeMirror } from "react-codemirror2";
import "codemirror/lib/codemirror.css";
import "codemirror/mode/javascript/javascript";
import "codemirror/theme/material.css";

export default function CodeEditor() {
  const [code, setCode] = useState("console.log('Hello, world!');");

  return (
    <div className="p-4 bg-gray-800 h-screen text-white">
      <h1 className="text-xl mb-4">Online Code Editor</h1>
      <CodeMirror
        value={code}
        options={{
          mode: "javascript",
          theme: "material",
          lineNumbers: true,
        }}
        onBeforeChange={(editor, data, value) => setCode(value)}
      />
      <button
        className="mt-4 p-2 bg-blue-500 rounded"
        onClick={() => eval(code)}
      >
        Run Code
      </button>
    </div>
  );
}
