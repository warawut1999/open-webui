// src/lib/storage.service.ts
import { KEYSECRET } from '$lib/constants';
import CryptoJS from 'crypto-js';

const SECRET_KEY = KEYSECRET;

export class StorageService {
  static secureStorage = {
    setItem: (key: string, value: any) => {
      const data = JSON.stringify(value);
      const encrypted = CryptoJS.AES.encrypt(data, SECRET_KEY).toString();
      localStorage.setItem(key, encrypted);
    },

    getItem: (key: string) => {
      const encrypted = localStorage.getItem(key);
      if (!encrypted) return null;

      try {
        const bytes = CryptoJS.AES.decrypt(encrypted, SECRET_KEY);
        const decrypted = bytes.toString(CryptoJS.enc.Utf8);
        return JSON.parse(decrypted);
      } catch (e) {
        console.error('Decryption failed', e);
        return null;
      }
    },

    removeItem: (key: string) => {
      localStorage.removeItem(key);
    },

    clearToken() {
        return localStorage.clear();
    }
  };
}
