---
records:
    - id: GQFCNY816R
      kind: series
      title: Grundlehren der mathematischen Wissenschaften
      expressions:
        - key: e1
          kind: edition
          ids:
            issn:
                - 0072-7830
                - 2196-9701
      scope:
        value: in
        rule: S4
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 0072-7830
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: GQFQTRCXDQ
      kind: monograph
      title: Séminaire de Théorie du Potentiel Paris, No. 9
      creators:
        - name: Nicolas Bouleau
          role: editor
        - name: Denis Feyel
          role: editor
        - name: Gabriel Mokobodzki
          role: editor
        - name: Francis Hirsch
          role: editor
      date: "1989"
      msc:
        - code: 00Bxx
          from: zbmath_search
        - code: 31-06
          from: zbmath_search
        - code: 35-06
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1989"
          ids:
            doi: 10.1007/bfb0085767
            zbl: "0671.00006"
            zbl_id: "194841"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1989"
              ids:
                isbn:
                    - "9783540515920"
                    - "9783540466758"
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
          native_id: 10.1007/bfb0085767
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "194841"
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
