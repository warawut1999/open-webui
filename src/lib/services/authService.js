import { AUTH_USER, USER_INFO } from "$lib/constants";

export class AuthService {
    constructor() {}

    setAuth(authUser) {
        localStorage.setJsonValue(AUTH_USER, JSON.stringify(authUser));
    }

    getAuth() {
       return localStorage.token;
    }

    setUser(user) {
        localStorage.setJsonValue(USER_INFO, JSON.stringify(user));
    }

    getUser() {
            return JSON.parse(localStorage.getJsonValue(USER_INFO));
    }
}

// export instance if needed
export const authService = new AuthService();
