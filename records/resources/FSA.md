---
records:
    - id: FSAJCEZ12S
      kind: monograph
      title: 'Arbeitstagung Bonn 1984: Proceedings of the meeting held by the Max-Planck-Institut für Mathematik, Bonn June 15–22, 1984'
      creators:
        - name: Friedrich Hirzebruch
          role: editor
        - name: Joachim Schwermer
          role: editor
        - name: Silke Suter
          role: editor
      date: "1985"
      msc:
        - code: 00Bxx
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: de
          date: "1985"
          ids:
            doi: 10.1007/bfb0084581
            zbl: "0547.00007"
            zbl_id: "3871215"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1985"
              ids:
                isbn:
                    - "9783540151951"
                    - "9783540392989"
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
          native_id: 10.1007/bfb0084581
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "3871215"
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
