import { createClient } from "@supabase/supabase-js";

const supabaseUrl = "https://hyocpesbblfsvvyprklt.supabase.co"
const supabaseKey = "sb_publishable_INMr00esz7G36349dkjJ8Q_Q-oCh04l"

export const supabase = createClient(
  supabaseUrl,
  supabaseKey
);
