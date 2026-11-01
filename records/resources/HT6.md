---
records:
    - id: HT6TV2BRR5
      kind: monograph
      title: Non-Commutative Harmonic Analysis
      creators:
        - name: Jacques Carmona
          role: editor
        - name: Michèle Vergne
          role: editor
      date: "1975"
      msc:
        - code: 00Bxx
          from: zbmath_search
        - code: 43-06
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: fr
          date: "1975"
          ids:
            doi:
                - 10.1007/bfb0063333
                - 10.1007/bfb0082191
                - 10.1007/bfb0087912
            zbl: "0299.00023"
            zbl_id: "3468714"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1979"
              ids:
                isbn:
                    - "9783540095163"
                    - "9783540351313"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1975"
              ids:
                isbn:
                    - "9783540071839"
                    - "9783540375241"
              access:
                class: record
            - key: m3
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1977"
              ids:
                isbn:
                    - "9783540082453"
                    - "9783540373650"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0063333
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0082191
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0087912
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "3468714"
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
