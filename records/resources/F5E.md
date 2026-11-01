---
records:
    - id: F5ENVJA9G5
      kind: monograph
      title: Séminaire Pierre Lelong — Henri Skoda (Analyse) Année 1976/77
      creators:
        - name: Pierre Lelong
          role: editor
        - name: Henri Skoda
          role: editor
      date: "1978"
      msc:
        - code: 00Bxx
          from: zbmath_search
        - code: 32-06
          from: zbmath_search
        - code: 31-06
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: fr
          date: "1978"
          ids:
            doi:
                - 10.1007/bfb0063241
                - 10.1007/bfb0097744
            zbl: "0345.00012"
            zbl_id: "3537610"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1978"
              ids:
                isbn:
                    - "9783540091011"
                    - "9783540355526"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1980"
              ids:
                isbn:
                    - "9783540102410"
                    - "9783540383208"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0063241
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0097744
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "3537610"
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
