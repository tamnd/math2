---
records:
    - id: EJJAEYSW3M
      kind: course
      title: Complex Analysis - I
      creators:
        - name: Arup Chattopadhyay
          role: instructor
      ids:
        course: 0022nd079:111103002
      expressions:
        - key: e1
          kind: edition
          language: en
          manifestations:
            - key: m1
              kind: page
              publisher: IIT Guwahati
              ids:
                nptel: "111103002"
              access:
                class: record
      scope:
        value: in
        rule: S6
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: nptel
          snapshot: blake3:89dc2ec164a0108adbecf0ec8c793929c947e196b164e762035d3fdd89a3f469
          native_id: "111103002"
          level: manifestation
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to deferred
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.4 scope/1
          note: from deferred to in
    - id: EJJTFCQFZC
      kind: monograph
      title: Spectral Methods of Automorphic Forms
      creators:
        - name: Henryk Iwaniec
          role: author
      date: "2002-11-19"
      msc:
        - code: 11F72
          from: zbmath_search
        - code: 11F12
          from: zbmath_search
        - code: 11F30
          from: zbmath_search
        - code: 11-02
          from: zbmath_search
        - code: 11M36
          from: zbmath_search
        - code: 58J50
          from: zbmath_search
        - code: 35P10
          from: zbmath_search
        - code: 11L05
          from: zbmath_search
        - code: 35P20
          from: zbmath_search
        - code: 11F66
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2002-11-19"
          ids:
            doi: 10.1090/gsm/053
            zbl: "1006.11024"
            zbl_id: "1860213"
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "2002-11-19"
              ids:
                isbn:
                    - "9780821831601"
                    - "9780821883921"
                    - "9781470417987"
              access:
                class: record
      relations:
        - kind: part_of
          to: YBEDX3XNVA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/gsm/053
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "1860213"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
---
