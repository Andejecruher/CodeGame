import { NextResponse } from 'next/server';

export function middleware(req) {
  const { pathname, origin } = req.nextUrl;

  if (pathname.includes('/auth')) {
    const token = req.cookies.get('token_codeGame');
    if (token) {
      return NextResponse.redirect(`${origin}/`);
    }
    return NextResponse.next();
  }

  if (pathname === '/' || pathname.startsWith('/dashboard')) {
    const token = req.cookies.get('token_codeGame');
    if (!token) {
      return NextResponse.redirect(`${origin}/auth/login`);
    }
    return NextResponse.next();
  }


  return NextResponse.next();
}