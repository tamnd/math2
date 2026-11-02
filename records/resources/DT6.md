---
records:
    - id: DT6TTQDKHA
      kind: monograph
      title: Fluid Dynamics
      creators:
        - name: H. Beirão da Veiga
          role: editor
      date: "1984"
      msc:
        - code: 00Bxx
          from: zbmath_search
        - code: 35-06
          from: zbmath_search
        - code: 76-06
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1984"
          ids:
            doi: 10.1007/bfb0072325
            zbl: "0523.00017"
            zbl_id: "3827777"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1984"
              ids:
                isbn:
                    - "9783540128939"
                    - "9783540387732"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 dev scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0072325
          level: work
        - source: zbmath_search
          snapshot: blake3:25dd7c4358839cf7c8c9f5d07f0562e94f38728153e7db2255a7191282b967c2
          native_id: "3827777"
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
          at: "2026-11-02"
          by: m2 v0.6.17 scope/1
          note: from in to in
---
