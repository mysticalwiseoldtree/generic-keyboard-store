import axios from "axios";

/**
 * Backend class for making requests to the backend.
 */
export class Backend {
  /**
   * Resolves the base URL of the backend.
   */
  static baseURL(): string {
    return "http://127.0.0.1:5000/";
  }

  /**
   * Sends a GET request to the backend.
   * @param url The URL to send the request to.
   * @returns The response from the backend.
   */
  static async get(url: string): Promise<string> {
    const response = await axios.get(this.baseURL() + url);
    return response.data as string;
  }
}
