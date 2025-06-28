import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ClarityModule } from '@clr/angular';
import { MonacoEditorModule } from 'ngx-monaco-editor-v2';
import { ProcessorService } from '../services/processor.service';
import { saveAs } from 'file-saver';
import { DatePipe } from '@angular/common';

@Component({
  selector: 'app-processing',
  imports: [ClarityModule, MonacoEditorModule, FormsModule],
  templateUrl: './processing.component.html',
  styleUrl: './processing.component.scss',
  providers: [DatePipe]
})
export class ProcessingComponent {

  code: string = "// Type in your JSON Array here";
  editorOptions = { theme: 'vs-dark', language: 'json', automaticLayout: true, fontSize: 14, fontFamily: 'Cascadia Code' };
  notification: { enabled: boolean, message?: string, type: string } = {
    enabled: false,
    message: undefined,
    type: 'success'
  };

  constructor(private processor: ProcessorService, private datePipe: DatePipe) { }

  fetchCSVForJSON() {
    try {
      const parsedJson = JSON.parse(this.code);
      this.processor.submitJsonData(parsedJson).subscribe({
        next: (result: Blob) => {
          this.setNotificationAlert('The CSV file has been generated successfully', 'success');
          const fileName = this.datePipe.transform(new Date(), 'ddMMyyyyhhmmss');
          saveAs(result, `${fileName}.csv`);
        },
        error: (error) => {
          this.setNotificationAlert(`Error processing JSON to CSV: ${error}`, 'warning');
        }
      });
    } catch (err) {
      this.setNotificationAlert('Invalid JSON content', 'warning');
    }
  }

  private setNotificationAlert(message: string, type: 'success' | 'warning', duration: number = 5000) {
    this.notification = {
      enabled: true,
      message: message,
      type: type
    };
    setTimeout(() => {
      this.notification = {
        enabled: false,
        message: undefined,
        type: undefined!
      };
    }, duration);
  }

}
