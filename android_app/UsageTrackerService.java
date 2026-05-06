package com.distraction.profiler;

import android.app.Service;
import android.content.Intent;
import android.os.IBinder;

public class UsageTrackerService extends Service {

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {

        // Track app usage here

        return START_STICKY;
    }

    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }
}