import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ClarityModule } from '@clr/angular';
import { MonacoEditorModule } from 'ngx-monaco-editor-v2';

@Component({
  selector: 'app-processing',
  imports: [ClarityModule, MonacoEditorModule, FormsModule],
  templateUrl: './processing.component.html',
  styleUrl: './processing.component.scss'
})
export class ProcessingComponent {

  code: string | null = "// Type in your JSON Array here";
  editorOptions = { theme: 'vs-dark', language: 'json', automaticLayout: true, fontSize: 14, fontFamily: 'Cascadia Code' };

}
